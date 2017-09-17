"""
class for rendering contexts required for most views.

contexts relating to user:
    school
"""

from django.views.generic import View


class BaseLabDashView(View):
    "Use this as basic class for context generation for all pages."
    # used for LoginRequiredMixin
    login_url = '/login/'

    def get_context(self, request):
        "overall context for all views method."
        context = {
            'school': None
        }
        if request.user.is_authenticated:
            context['school'] = request.user.profile.school
        return context
