from baselabwatch.views import DashboardBase
from baselabwatch.serializers import StudentSerializer
from baselabwatch.forms import XMLFileUploadForm
from baselabwatch.views import XMLUploadView
from django.shortcuts import redirect
from django.urls import reverse
from json import loads
from urllib.parse import urlencode

class StudentView(DashboardBase):
    template_name = 'base/studentadmin.html'
    current_app = 'baselabwatch'
    serializer = StudentSerializer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['upload_form'] = XMLFileUploadForm
        return context

    def post(self, *args, **kwargs):
        uploadResponse = XMLUploadView.post(self, *args, **kwargs)
        return redirect(reverse('baselabwatch:student') + '?tab=upload&upload=true&' + urlencode(loads(uploadResponse.content.decode())))
