from baselabwatch.views import DashboardBase
from logger.models import Kiosk, StudentSession
from baselabwatch.models import Student
from logger.forms import LogForm
from logger.util import log_student


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

class ClientView(DashboardBase):
    "Client view"

    template_name = "kiosk/search.html"
    uuid_template_name = "kiosk/kiosk.html"
    current_app = "logger"

    def get(self, request, uuid=None):
        "Basic GET"
        if uuid:
            return render(request, self.uuid_template_name, {
                "uuid": uuid,
                "kiosk": get_object_or_404(Kiosk, auth_code=uuid)
            })
        return super().get(request)

    def post(self, request, uuid=None):
        "Incoming data should be in parsed through log form"
        print(uuid)
        if uuid:
            form = LogForm(request.POST)
            if form.is_valid():
                student = get_object_or_404(Student, pk=form.cleaned_data['pk'])
                status = log_student(student, form.mode)
                return JsonResponse({
                    'data': form.data, 
                    'student': student.first_name + ' ' + student.last_name, 
                    'status': status,
                    'mode': form.mode
                })
            else:
                response = JsonResponse({'errors': form.errors, 'data': form.data})
                response.status_code = 400
                return response
        return self.get(request)
