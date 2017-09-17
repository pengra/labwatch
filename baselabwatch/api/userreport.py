from baselabwatch.models import UserReport
from baselabwatch.serializers import UserReportSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class UserReportViewSet(viewsets.ModelViewSet):
    "Viewsets for User reports."
    queryset = UserReport.objects.all()
    serializer_class = UserReportSerializer
    permission_classes = (IsAdminUser,)
