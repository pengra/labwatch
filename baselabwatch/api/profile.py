from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from baselabwatch.models import Profile
from baselabwatch.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    "Viewsets for Profiles."
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser,)