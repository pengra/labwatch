"""
class for rendering contexts required for most views.

contexts relating to user:
    school
"""

from django.views.generic import View, TemplateView 

class DashboardBase(TemplateView):
    template_name = 'base/_base.html'

    def post(self, request, *args, **kwargs):
        "Handle post requests."
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)