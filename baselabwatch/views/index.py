from django.views.generic import View, TemplateView

class IndexView(TemplateView):
    template_name = "base/coverpage.html"

    def post(self, *args, **kwargs):
        from django.core.mail import mail_admins
        email = self.request.POST.get('email')
        mail_admins(
            '[sign up]',
            'Someone signed up with: ' + email,
        )
        context = self.get_context_data(**kwargs)
        context['signed_up'] = True
        return self.render_to_response(context)