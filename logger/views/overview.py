from baselabwatch.views import DashboardBase
from logger.serializers import StudentSessionSerializer
from logger.models import StudentSession

class OverviewView(DashboardBase):
    template_name = "logger/overview.html"
    current_app = "logger"
    serializer = StudentSessionSerializer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['serializer'] = StudentSessionSerializer(
            context={'request': self.request}
        )
        return context