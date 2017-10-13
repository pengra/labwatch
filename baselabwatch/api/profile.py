from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import JSONRenderer
from baselabwatch.models import Profile
from baselabwatch.serializers import ProfileSerializer
from baselabwatch.permissions import ProfilePermission

class ProfileViewSet(viewsets.ModelViewSet):
    "Viewsets for Profiles."
    serializer_class = ProfileSerializer
    permission_classes = (ProfilePermission, )
    # renderer_classes = [JSONRenderer]

    def get_queryset(self):
        if self.request.user:
            return Profile.objects.filter(user=self.request.user)
        return []
