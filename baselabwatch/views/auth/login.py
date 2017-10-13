from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import redirect, render

def login_view(request, *args, **kwargs):
    print(request)
    context = {}
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username', ''), password=request.POST.get('password', ''))
        if user is not None:
            login(request, user)
            return redirect(reverse('baselabwatch:index'))
        else:
            context['error'] = True
    
    return render(request, 'auth/login.html', context)