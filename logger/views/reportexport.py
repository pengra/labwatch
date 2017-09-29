import json

from django.http.response import HttpResponse
from django.views.generic import View

from pytz import timezone
from datetime import datetime
from labwatch.settings import TIME_ZONE
from logger.forms import ExportForm
from logger.util import export_logs


class ReportExportView(View):
    "View for excel export"

    def get(self, request):
        if not request.user.is_authenticated():
            response = HttpResponse(json.dumps(
                {"errors": ["Not authenticated"]}), content_type='application/json')
            response.status_code = 403
            return response

        if not request.user.profile.school:
            response = HttpResponse(json.dumps(
                {"errors": ["Not associated with any school"]}), content_type='application/json')
            response.status_code = 403
            return response

        form = ExportForm(request.GET)
        if form.is_valid():
            download = export_logs(form.cleaned_data, self.request.user.profile.timezone)
            if download:
                # Mime type data:
                # https://blogs.msdn.microsoft.com/vsofficedeveloper/2008/05/08/office-2007-file-format-mime-types-for-http-content-streaming-2/
                now = datetime.now(timezone(TIME_ZONE))
                filename = "{}.logs.{}-{}-{}".format(
                    request.user.profile.school.short_name,
                    now.year, now.month, now.day
                )
                response = HttpResponse(
                    download.read(),
                    content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(
                    filename)

                return response

            response = HttpResponse(json.dumps(
                {"errors": ["No columns selected"]}))
            response.status_code = 400
            return response

        else:
            response = HttpResponse(json.dumps(form.errors))
            response.status_code = 400
            return response
