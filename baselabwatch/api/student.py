from baselabwatch.models import Student
from baselabwatch.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class StudentViewSet(viewsets.ModelViewSet):
    "Viewsets for Students."
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminUser,)
