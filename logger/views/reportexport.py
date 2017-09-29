from django.views.generic import View
from django.http.response import HttpResponse
import json

class ReportExportView(View):
    
    def post(self, request):
        
        return HttpResponse(json.dumps({"data": request.POST}))