from baselabwatch.views import DashboardBase
from baselabwatch.serializers import SchoolSerializer
from baselabwatch.models import School

class SchoolView(DashboardBase):
    template_name = 'base/schooladmin.html'
    current_app = 'baselabwatch'
    serializer = SchoolSerializer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if context['serializer']:
            context['serializer'] = context['serializer'](
                instance=self.request.user.profile.school,
                context={'request': self.request}
            )
        context['students'] = self.request.user.profile.school.student_set.all().count()
        return context
