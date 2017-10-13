from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect(reverse('index'))