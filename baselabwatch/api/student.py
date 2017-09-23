from baselabwatch.models import Student
from baselabwatch.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class StudentViewSet(viewsets.ModelViewSet):
    "Viewsets for Students."
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminUser,)
    # renderer_classes = [JSONRenderer]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile.school)
