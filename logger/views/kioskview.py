from baselabwatch.views import DashboardBase
from logger.serializers import KioskSerializer, PollChoiceSerializer, PollQuestionSerializer
from logger.forms import KioskForm
from django.http.response import JsonResponse

class KioskView(DashboardBase):
    template_name = "logger/kioskview.html"
    current_app = "logger"
    serializer = [KioskSerializer, PollQuestionSerializer, PollChoiceSerializer]

    def post(self, request, *args, **kwargs):
        "Handle post requests."
        form = KioskForm(request.POST)
        response = {}
        status_code = None
        
        if form.is_valid():
            response['data'] = form.cleaned_data
            status_code = 200
        else:
            response['errors'] = form.errors
            status_code = 400

        http_response = JsonResponse(response)
        http_response.status_code = status_code
        return http_response
        