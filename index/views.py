"""
the Index app basically serves as the primary location for
all forms and views. These are all the generic views.
"""
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.views.generic import TemplateView, View

from random import shuffle

from index import forms
from polls.models import PollChoice, PollQuestion
from logger.models import Student, Log
from registration.models import Kiosk, School


class CoverView(TemplateView):
    "Primary view."
    template_name = 'index/coverpage.html'


class BaseLabDashView(View):
    "Use this as basic class for context generation for all pages."
    # used for LoginRequiredMixin
    login_url = '/login/'

    def get_context(self, request):
        "overall context for all views method."
        context = {
            "is_authenticated": request.user.is_authenticated(),
            'is_engineer': False,
            'is_librarian': False,
            'is_teacher': False,
            'school': None
        }
        if context['is_authenticated']:
            context['is_engineer'] = len(
                request.user.groups.filter(name__in=['Engineer']))
            context['is_librarian'] = len(
                request.user.groups.filter(name__in=['Librarian']))
            context['is_teacher'] = len(
                request.user.groups.filter(name__in=['Teacher']))

            context['school'] = request.user.associated_school.first()

        return context


class LoginView(BaseLabDashView):
    "Login for everyone view."

    def get(self, request):
        "Basic view for login,"
        context = self.get_context(request)

        if context['is_authenticated']:
            return redirect('index:index')

        return render(request, 'index/login.html', context)

    def post(self, request):
        "Handling user login."
        context = self.get_context(request)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index:dashboard')
        else:
            # Change context upon invalid login
            context['error'] = "Invalid Credentials"

        return render(request, 'index/login.html', context)


class DashboardView(LoginRequiredMixin, BaseLabDashView):
    "View for dashboard."

    def get(self, request):
        "View for dashboard."
        context = self.get_context(request)

        if context['school']:
            context['logged_in_students'] = Student.objects.filter(
                school=context['school'], signed_in=True
            )
            context['kiosk_active'] = len(
                context['school'].kiosk_set.filter(active=True)) >= 1

        return render(request, 'dashboard/index.html', context)


class DashboardKioskView(LoginRequiredMixin, BaseLabDashView):
    "View for kiosk management."

    def get_random_code(self):
        "Random code generation."
        potential_code = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
            '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        shuffle(potential_code)
        return "".join(potential_code)[:32]

    def get_context(self, request):
        context = super().get_context(request)

        # loop until unique code recieved
        # Very bad practice.
        while True:
            code = self.get_random_code()
            if not Kiosk.objects.filter(auth_code=code):
                break

        context['potential_code'] = code
        context['kiosks'] = context['school'].kiosk_set.all()
        context['primary_contact'] = request.user.associated_school.get(
        ).primary_contact

        return context

    def get(self, request):
        "View for kiosk management."
        context = self.get_context(request)
        return render(request, 'dashboard/kiosk.html', context)

    def post(self, request):
        "Manipulating kiosk objects."
        context = self.get_context(request)

        kiosk_put_form = forms.KioskForm(request.POST)
        if kiosk_put_form.is_valid():
            proxy_method = kiosk_put_form.cleaned_data.get(
                'proxy_method').lower()
            if proxy_method == '':  # (put)
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


class KioskView(View):
    "General view for kiosks."

    def get(self, request, auth_code):
        "Get view."
        kiosk = get_object_or_404(Kiosk, auth_code=auth_code)
        pollquestion = PollQuestion.objects.filter(
            kiosk=Kiosk.objects.get(auth_code=auth_code)).last()

        if pollquestion:
            poll_a = pollquestion.pollchoice_set.filter(active=True)
        else:
            poll_a = []

        return render(request, 'kiosk/_base.html', {
            "kiosk": kiosk,
            "school": kiosk.school,
            "poll_q": pollquestion,
            "poll_a": poll_a,
        })

    def post(self, request, auth_code):
        "Post ajax response."
        school = get_object_or_404(Kiosk, auth_code=auth_code).school

        client_data = forms.LoginForm(request.POST)
        response = {
            'input_mode': -1,
            'student': None
        }
        found = False

        # Student scanned their card
        if client_data.is_valid_card_number():
            student = get_object_or_404(
                Student, student_id=client_data.cleaned_data['return_value'],
                school=school)
            response['input_mode'] = 0

            found = True

        # Student typed in an email
        if not found and client_data.is_valid_email():
            student = get_object_or_404(
                Student, email=client_data.cleaned_data['return_value'],
                school=school)
            response['input_mode'] = 2

            found = True

        # Student typed in their nickname
        if not found and client_data.is_valid_nickname():
            name = client_data.cleaned_data['return_value']
            nickname = Student.objects.filter(
                nick_name__iexact=name, school=school)

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
                first_name__iexact=fname, last_name__iexact=lname.replace(' ', ''), school=school)
            spaces = Student.objects.filter(
                first_name__iexact=fname, last_name__iexact=lname, school=school)

            # Get student or 404
            if len(no_spaces):
                student = no_spaces[0]
                response['input_mode'] = 1
                found = True
            elif len(spaces):
                student = spaces[0]
                response['input_mode'] = 1
                found = True

        if found:

            # Create response
            response['student'] = {
                "fname": student.first_name,
                "status_before_sign": student.signed_in,
                "pk": student.pk,
                "school": str(school),
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


class KioskPollView(View):
    "View just for poll submissions"

    def post(self, request, auth_code):
        "View just for poll submissions"
        pollquestion = PollQuestion.objects.filter(
            kiosk=Kiosk.objects.get(auth_code=auth_code)).last()

        poll_response = forms.LoginForm(request.POST)

        if poll_response.is_valid_poll():
            answer = pollquestion.pollchoice_set.filter(
                choice_text__iexact=poll_response.cleaned_data['return_value'],
                active=True)

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
                    kiosk = get_object_or_404(
                        Kiosk, pk=poll_form.cleaned_data['pk'])

                    question = PollQuestion(
                        question_text=poll_form.cleaned_data['question'],
                    )
                    question.save()
                    question.kiosk.add(kiosk)
                    question.save()

                    answers = poll_form.cleaned_data['answers']
                    answers = answers.replace('\r', '').split('\n')

                    for item in answers:
                        poll = PollChoice(choice_text=item, question=question)
                        poll.save()

                elif poll_form.cleaned_data['method_proxy'] == 'PUT':
                    kiosk = get_object_or_404(
                        Kiosk, pk=poll_form.cleaned_data['pk'])
                    question = kiosk.pollquestion_set.last()
                    question.question_text = poll_form.cleaned_data['question']
                    question.save()

                    new_answers = poll_form.cleaned_data['answers'].replace(
                        '\r', '').split('\n')

                    # delete the choices that the user deleted
                    for choice in question.pollchoice_set.filter(active=True):
                        if choice.choice_text not in new_answers:
                            choice.active = False
                            choice.save()

                    # add new choices that the user requested
                    for choice in new_answers:
                        if not PollChoice.objects.filter(choice_text=choice, active=True):
                            PollChoice(
                                question=question,
                                choice_text=choice
                            ).save()

                elif poll_form.cleaned_data['method_proxy'] == 'DELETE':
                    kiosk = get_object_or_404(
                        Kiosk, pk=poll_form.cleaned_data['pk'])

                    question = kiosk.pollquestion_set.last()
                    question.kiosk.clear()
                    question.save()

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

        if request.method == 'POST':
            # prevent the user from refreshing and mass creating a bunch polls
            return redirect('index:dashboard-poll')

        return render(request, 'dashboard/poll.html', context)

    return redirect('index:login')


def dashboard_student_bulk_view(request):
    "view for uploading students by excel sheet."
    context = {
        'is_librarian': len(request.user.groups.filter(name__in=['Librarian'])),
        'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
    }
    if request.user.is_authenticated():
        school = request.user.associated_school.get()
        context['school'] = school

        return render(request, 'dashboard/bulk.html', context)

    return redirect('index:login')


def dashboard_student_admin_view(request):
    "View for individual student tweaking."
    context = {
        'is_librarian': len(request.user.groups.filter(name__in=['Librarian'])),
        'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
    }
    if request.user.is_authenticated():
        school = request.user.associated_school.get()
        context['school'] = school

        return render(request, 'dashboard/studentadmin.html', context)

    return redirect('index:login')
