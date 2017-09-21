from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import JSONRenderer
from baselabwatch.models import School
from baselabwatch.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    "Viewsets for Schools."
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAdminUser,)
    # renderer_classes = [JSONRenderer]

    def perform_create(self, serializer):
        school = serializer.save(primary_contact=self.request.user)
        profile = self.request.user.profile
        profile.school = school
        profile.save()