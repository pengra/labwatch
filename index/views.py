from django.shortcuts import render

# Create your views here.

def cover_view(request):
    "Primary view."
    return render(request, 'index/coverpage.html')
