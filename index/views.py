"""
the Index app basically serves as the primary location for
all forms and views. These are all the generic views.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from index import forms
from registration.models import Kiosk


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
        context = {
            'school': request.user.associated_school.get(),
            'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
        }
        return render(request, 'dashboard/index.html', context)

    # user is not authenticated, redirect them to login page
    return redirect('index:login')


def dashboard_kiosk_view(request):
    "View for kiosk management."

    context = {}

    if request.user.is_authenticated:
        school = request.user.associated_school.get()
        context = {
            'school': school,
            'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
            'kiosks': school.kiosk_set.all(),
            'is_librarian': len(request.user.groups.filter(name__in=['Librarian'])),
            'primary_contact': request.user.associated_school.get().primary_contact,
        }

        if request.method == 'POST':
            kiosk_put_form = forms.KioskForm(request.POST)
            if kiosk_put_form.is_valid():
                existing_kiosk = Kiosk.objects.get(
                    pk=kiosk_put_form.cleaned_data['pk'],
                    auth_code=kiosk_put_form.cleaned_data['auth_code']
                )

                existing_kiosk.name = kiosk_put_form.cleaned_data['name']
                existing_kiosk.active = kiosk_put_form.cleaned_data['active'].lower(
                ) == 'true'
                existing_kiosk.save()

        return render(request, 'dashboard/kiosk.html', context)

    # user is not authenticated, redirect them to login page
    return redirect('index:login')
