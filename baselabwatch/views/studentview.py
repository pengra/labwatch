from baselabwatch.views import DashboardBase
from baselabwatch.serializers import StudentSerializer

class StudentView(DashboardBase):
    template_name = 'base/studentadmin.html'
    current_app = 'baselabwatch'
    serializer = StudentSerializer

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     if context['serializer']:
    #         context['serializer'] = context['serializer'](
    #             instance=self.request.user.profile.school,
    #             context={'request': self.request}
    #         )
    #     return context