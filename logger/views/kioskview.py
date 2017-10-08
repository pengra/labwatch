from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse

from baselabwatch.views import DashboardBase
from logger.util import update_poll
from logger.forms import KioskForm
from logger.models import Kiosk
from logger.serializers import (KioskSerializer, PollChoiceSerializer,
                                PollQuestionSerializer)


class KioskView(DashboardBase):
    template_name = "logger/kioskview.html"
    current_app = "logger"
    serializer = [KioskSerializer,
                  PollQuestionSerializer, PollChoiceSerializer]

    def post(self, request, *args, **kwargs):
        "Handle post requests."
        if not request.user.is_authenticated():
            response = JsonResponse(
                {"errors": ["Not authenticated"]}, content_type='application/json')
            response.status_code = 403
            return response

        if not request.user.profile.school:
            response = JsonResponse(
                {"errors": ["Not associated with any school"]}, content_type='application/json')
            response.status_code = 403
            return response

        form = KioskForm(request.POST)
        response = {}
        status_code = None

        if form.is_valid():
            status_code = 201

            # Update the form
            try:
                kiosk = Kiosk.objects.get(pk=form.cleaned_data['kiosk_pk'])
                kiosk.name = form.cleaned_data['name']
                kiosk.poll = update_poll(
                    kiosk,
                    form.cleaned_data['poll_question'],
                    form.cleaned_data['poll_choices']
                )
                kiosk.save()
            except ObjectDoesNotExist:
                response['errors'] = 'PK not found'
                response['data'] = form.cleaned_data
                status_code = 404

        else:
            response['errors'] = form.errors
            status_code = 400

        http_response = JsonResponse(response)
        http_response.status_code = status_code
        return http_response
