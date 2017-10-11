from baselabwatch.views import DashboardBase
from logger.models import Kiosk
from logger.forms import LogForm

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

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

    def post(self, request, uuid=None):
        if uuid:
            "Incoming data should be in parsed through log form"
            form = LogForm(request.POST)
            if form.is_valid():
                JsonResponse({})
        return self.get(request)