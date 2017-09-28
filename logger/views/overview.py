from baselabwatch.views import DashboardBase
from logger.serializers import StudentSessionSerializer
from logger.models import StudentSession

class OverviewView(DashboardBase):
    template_name = "logger/overview.html"
    current_app = "logger"
    serializer = StudentSessionSerializer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # import pdb; pdb.set_trace()
        context['serializer'] = StudentSessionSerializer(
            # instance=StudentSession.objects.get(),
            context={'request': self.request}
        )
        return context