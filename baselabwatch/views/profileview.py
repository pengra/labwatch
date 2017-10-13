from baselabwatch.views import DashboardBase
from baselabwatch.serializers import ProfileSerializer

class ProfileView(DashboardBase):
    template_name = 'base/profileadmin.html'
    current_app = 'baselabwatch'
    serializer = ProfileSerializer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if context['serializer']:
            context['serializer'] = context['serializer'](
                instance=self.request.user.profile,
                context={'request': self.request}
            )
        return context