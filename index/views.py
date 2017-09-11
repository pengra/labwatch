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
            logged_in = Student.objects.filter(
                school=schools[0], signed_in=True)
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
            'input_mode': -1,
            'student': None
        }
        found = False

        # Student scanned their card
        if client_data.is_valid_card_number():
            student = get_object_or_404(
                Student, student_id=client_data.cleaned_data['return_value'])
            response['input_mode'] = 0

            found = True

        # Student typed in an email
        if not found and client_data.is_valid_email():
            student = get_object_or_404(
                Student, email=client_data.cleaned_data['return_value'])
            response['input_mode'] = 2

            found = True

        # Student typed in their nickname
        if not found and client_data.is_valid_nickname():
            name = client_data.cleaned_data['return_value']
            nickname = Student.objects.filter(nick_name__iexact=name)

            if len(nickname):
                student = nickname[0]
                response['input_mode'] = 3
                found = True

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
                response['input_mode'] = 1
            elif len(spaces):
                student = spaces[0]
                response['input_mode'] = 1
            else:
                raise Http404()

            found = True

        if found:

            # Create response
            response['student'] = {
                "fname": student.first_name,
                "status_before_sign": student.signed_in,
                "pk": student.pk,
            }

            # opposite, so if student was signed in, they're
            # now signing out.
            signing_out = student.signed_in

            # toggle sign in status
            student.signed_in = not student.signed_in
            student.save()

            # create log
            log = Log(
                student=student,
                mode=Log.SIGN_MODE[signing_out][0],
                input_mode=Log.INPUT_MODE[response['input_mode']][0],
            )
            log.save()
            response['log'] = log.pk
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
            'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
        }
        return render(request, 'kiosk/_base.html', context)


def kiosk_poll_view(request, auth_code):
    "View just for poll submissions"
    if request.method == 'POST':
        pollquestion = PollQuestion.objects.filter(
            kiosk=Kiosk.objects.get(auth_code=auth_code)).last()

        poll_response = forms.LoginForm(request.POST)

        if poll_response.is_valid_poll():
            answer = pollquestion.pollchoice_set.filter(
                choice_text__iexact=poll_response.cleaned_data['return_value'])

            if answer:
                # Update log with choice
                log = get_object_or_404(
                    Log, pk=poll_response.cleaned_data['log_pk'])
                log.poll_answer = answer[0]
                log.save()

                # Update pollchoice vote count
                answer[0].votes = answer[0].votes + 1
                answer[0].save()

                return JsonResponse({"okay": True, "question": str(pollquestion), "answer": str(answer[0])})

    # Never handle non-post queries
    raise Http404


def kiosk_ping_json(request, auth_code):
    "View just for pinging."
    return JsonResponse({
        'enabled': Kiosk.objects.get(auth_code=auth_code).active
    })


def dashboard_poll_view(request):
    "For poll management."
    context = {
        'is_librarian': len(request.user.groups.filter(name__in=['Librarian'])),
        'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
    }
    if request.user.is_authenticated():
        school = request.user.associated_school.filter()
        
        if request.method == 'POST':
            # Aight so it's a form coming through
            poll_form = forms.PollMangementForm(request.POST)
            if poll_form.is_valid():
                if poll_form.cleaned_data['method_proxy'] == 'CREATE':
                    # creating a new poll
                    kiosk = get_object_or_404(Kiosk, pk=poll_form.cleaned_data['pk'])
                    question = PollQuestion(
                        question_text=poll_form.cleaned_data['question'],
                    )
                    question.save()
                    question.kiosk.add(kiosk)
                    question.save()

                    answers = poll_form.cleaned_data['answers']
                    answers = answers.replace('\r', '').split('\n')

                    for item in answers:
                        PollChoice(
                            choice_text=item,
                            question=question
                        ).save()

                elif poll_form.cleaned_data['method_proxy'] == 'PUT':
                    # editing an old poll
                    pass
            else:
                context['form_error'] = "Invalid Form Submission. Try again."
                    
        if school:
            poll_management_context = []

            for kiosk in school[0].kiosk_set.all():
                question = kiosk.pollquestion_set.last()
                if question:
                    answers = question.pollchoice_set.all()
                else:
                    answers = None

                poll_management_context.append([kiosk, question, answers])

            context["school"] = school[0]
            context["kiosks"] = poll_management_context

        return render(request, 'dashboard/poll.html', context)

    return redirect('index:login')
