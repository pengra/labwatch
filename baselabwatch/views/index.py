from django.views.generic import View, TemplateView

class IndexView(TemplateView):
    template_name = "base/coverpage.html"

class LoginView(TemplateView):
    template_name = 'base/login.html'

class SignupView(TemplateView):
    template_name = 'base/signup.html'