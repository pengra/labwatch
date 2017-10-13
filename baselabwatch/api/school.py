from rest_framework import viewsets
from rest_framework.response import Response
from baselabwatch.models import School
from baselabwatch.serializers import SchoolSerializer
from baselabwatch.permissions import SchoolPermission
from django.shortcuts import get_object_or_404


class SchoolViewSet(viewsets.ModelViewSet):
    "Viewsets for Schools."
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (SchoolPermission,)
    # renderer_classes = [JSONRenderer]

    def perform_create(self, serializer):
        school = serializer.save(primary_contact=self.request.user)
        profile = self.request.user.profile
        profile.school = school
        profile.save()