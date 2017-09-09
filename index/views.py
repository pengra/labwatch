from django.shortcuts import render

# Create your views here.

def cover_view(request):
    "Primary view."
    return render(request, 'index/coverpage.html')

def login_view(request):
    "Login for everyone view."
    return render(request, 'index/login.html')
