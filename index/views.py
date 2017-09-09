from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.


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
        school =  request.user.associated_school.get()
        context = {
            'school': school,
            'is_engineer': len(request.user.groups.filter(name__in=['Engineer'])),
            'kiosks': school.kiosk_set.all(),
        }
        return render(request, 'dashboard/kiosk.html', context)

    # user is not authenticated, redirect them to login page
    return redirect('index:login')
