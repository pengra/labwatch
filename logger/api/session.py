from logger.models import StudentSession
from logger.serializers import StudentSessionSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class StudentSessionViewSet(viewsets.ModelViewSet):
    "Viewsets for Users."
    queryset = StudentSession.objects.all()
    serializer_class = StudentSessionSerializer
    permission_classes = (IsAdminUser,)
