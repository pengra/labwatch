from baselabwatch.models import UserReport
from baselabwatch.serializers import UserReportSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import JSONRenderer

class UserReportViewSet(viewsets.ModelViewSet):
    "Viewsets for User reports."
    queryset = UserReport.objects.all()
    serializer_class = UserReportSerializer
    permission_classes = (IsAdminUser,)
    # renderer_classes = [JSONRenderer]
