"""
class for rendering contexts required for most views.

contexts relating to user:
    school
"""

from django.views.generic import View, TemplateView 
from baselabwatch.util import get_app_metadata

class DashboardBase(TemplateView):
    template_name = 'base/_base.html'
    current_app = 'baselabwatch'
    serializer = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['current_app'] = self.current_app
        if self.serializer:
            context['serializer'] = self.serializer
        return context

    def post(self, request, *args, **kwargs):
        "Handle post requests."
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)