from baselabwatch.views import DashboardBase
from logger.models import Kiosk
from django.shortcuts import render, get_object_or_404

class ClientView(DashboardBase):
    "Client view"

    template_name = "kiosk/search.html"
    uuid_template_name = "kiosk/kiosk.html"
    current_app = "logger"

    def get(self, request, uuid=None):
        if uuid:
            return render(request, self.uuid_template_name, {
                "uuid": uuid,
                "kiosk": get_object_or_404(Kiosk, auth_code=uuid)
            })
        return super().get(request)
        