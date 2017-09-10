"""
the Index app basically serves as the primary location for
all forms and views. These are all the generic views.
"""
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, Http404

from random import shuffle

from index import forms
from polls.models import PollChoice, PollQuestion
from logger.models import Student, Log
from registration.models import Kiosk, School


def cover_view(request):
    "Primary view."
    return render(request, 'index/coverpage.html')


def login_view(request):
    "Login for everyone view."

    # If the user is already authenticated
    # take them to the home page
    if request.user.is_authenticated:
        return redirect('index:index')

    context = {}

    # handle authentication requests via django auth.login/authenticate
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Upon succesful authentication, redirect to homepage
            return redirect('index:dashboard')
        else:
            # Change context upon invalid login
            context = {
                "error": "Invalid Credentials"
            }

    # If made it all the way to the end, spew out
    # login form with context.
    return render(request, 'index/login.html', context)


def dashboard_view(request):
    "View for dashboards for librarians."

    context = {}

    if request.user.is_authenticated:
        schools = request.user.associated_school.all()

        if len(schools) == 0:
            context = {
                'school': False
            }
        else:
            logged_in = Student.objects.filter(school=schools[0], signed_in=True)
            context = {
                'school': schools[0],
                'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
                'logged_in_students': logged_in,
                'len_students': len(logged_in),
                'kiosk_active': len(schools[0].kiosk_set.filter(active=True)),
            }
        
        return render(request, 'dashboard/index.html', context)

    # user is not authenticated, redirect them to login page
    return redirect('index:login')


def dashboard_kiosk_view(request):
    "View for kiosk management."

    context = {}
    potential_code = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
        '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    shuffle(potential_code)

    while len(Kiosk.objects.filter(auth_code="".join(potential_code)[:32])) > 1:
        shuffle(potential_code)

    if request.user.is_authenticated:
        school = request.user.associated_school.get()
        context = {
            'school': school,
            'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
            'kiosks': school.kiosk_set.all(),
            'is_librarian': len(request.user.groups.filter(name__in=['Librarian'])),
            'primary_contact': request.user.associated_school.get().primary_contact,
            'potential_code': "".join(potential_code)[:32],
        }

        if request.method == 'POST':
            kiosk_put_form = forms.KioskForm(request.POST)
            if kiosk_put_form.is_valid():
                proxy_method = kiosk_put_form.cleaned_data.get(
                    'proxy_method').lower()
                if proxy_method == '':
                    existing_kiosk = Kiosk.objects.get(
                        pk=kiosk_put_form.cleaned_data['pk'],
                        auth_code=kiosk_put_form.cleaned_data['auth_code']
                    )

                    existing_kiosk.name = kiosk_put_form.cleaned_data['name']
                    existing_kiosk.active = kiosk_put_form.cleaned_data['active'].lower(
                    ) == 'true'
                    existing_kiosk.save()
                elif proxy_method == 'delete':
                    kiosk = Kiosk.objects.get(
                        pk=kiosk_put_form.cleaned_data['pk'],
                        auth_code=kiosk_put_form.cleaned_data['auth_code'],
                        name=kiosk_put_form.cleaned_data['name']
                    )
                    kiosk.delete()
                elif proxy_method == 'create':
                    kiosk = Kiosk(
                        auth_code=kiosk_put_form.cleaned_data['auth_code'],
                        name=kiosk_put_form.cleaned_data['name'],
                        active=kiosk_put_form.cleaned_data['active'].lower(
                        ) == 'true',
                        school=School.objects.get(
                            name=kiosk_put_form.cleaned_data['school'])
                    )
                    kiosk.save()

        return render(request, 'dashboard/kiosk.html', context)

    # user is not authenticated, redirect them to login page
    return redirect('index:login')


def kiosk_view(request, auth_code=None):
    "Default view for kiosks. Point chromium locks here."

    if request.method == 'POST':

        client_data = forms.LoginForm(request.POST)
        response = {
            'card': False,
            'email': False,
            'name': False,
            'nick': False,
            'student': None
        }
        found = False

        # Student scanned their card
        if client_data.is_valid_card_number():
            student = get_object_or_404(
                Student, student_id=client_data.cleaned_data['return_value'])
            response['card'] = True
            response['student'] = {
                "fname": student.first_name,
                "status_before_sign": student.signed_in,
            }
            found = True

        # Student typed in an email
        if not found and client_data.is_valid_email():
            student = get_object_or_404(
                Student, email=client_data.cleaned_data['return_value'])
            response['email'] = True
            response['student'] = {
                "fname": student.first_name,
                "status_before_sign": student.signed_in
            }
            found = True

        # Student typed in their nickname
        if not found and client_data.is_valid_nickname():
            name = client_data.cleaned_data['return_value']
            nickname = Student.objects.filter(nick_name__iexact=name)

            if len(nickname):
                student = nickname[0]
                response['nick'] = True
                found = True

                response['student'] = {
                    'fname': student.first_name,
                    'status_before_sign': student.signed_in
                }


        # Student typed in their name
        if not found and client_data.is_valid_name():
            name = client_data.cleaned_data['return_value']
            fname = name.split(' ', 1)[0]
            lname = name.split(' ', 1)[1]

            no_spaces = Student.objects.filter(
                first_name__iexact=fname, last_name__iexact=lname.replace(' ', ''))
            spaces = Student.objects.filter(
                first_name__iexact=fname, last_name__iexact=lname)

            # Get student or 404
            if len(no_spaces):
                student = no_spaces[0]
                response['name'] = True
            elif len(spaces):
                student = spaces[0]
                response['name'] = True
            else:
                raise Http404()

            response['student'] = {
                'fname': student.first_name,
                'status_before_sign': student.signed_in
            }

            found = True

        if found:
            return JsonResponse(response)

        raise Http404

    else:
        kiosk = get_object_or_404(Kiosk, auth_code=auth_code)
        pollquestion = PollQuestion.objects.filter(
            kiosk=Kiosk.objects.get(auth_code=auth_code)).last()
        if pollquestion:
            poll_a = pollquestion.pollchoice_set.all()
        else:
            poll_a = []
        context = {
            "kiosk": kiosk,
            "school": kiosk.school,
            "poll_q": pollquestion,
            "poll_a": poll_a,
        }
        return render(request, 'kiosk/_base.html', context)


def kiosk_poll_view(request, auth_code):
    "View just for poll submissions"
    if request.method == 'POST':
        pollquestion = PollQuestion.objects.filter(
            kiosk=Kiosk.objects.get(auth_code=auth_code)).last()

        poll_response = forms.LoginForm(request.POST)

        if poll_response.is_valid_poll():
            answer = pollquestion.pollchoice_set.filter(choice_text__iexact=poll_response.cleaned_data['return_value'])
            if answer:
                return JsonResponse({"okay": True, "question": str(pollquestion), "answer": str(answer[0])})
            return JsonResponse({"okay": False, 'question': str(pollquestion)})

        return JsonResponse({"okay": False})

    # Never handle non-post queries
    raise Http404

def kiosk_ping_json(request, auth_code):
    "View just for pinging."
    return JsonResponse({
        'enabled': Kiosk.objects.get(auth_code=auth_code).active
    })