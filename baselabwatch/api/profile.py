from django.contrib.auth.models import User
from baselabwatch.serializers.user import ProfileSerializer
from baselabwatch.util.permissions import ProfilePermission
from rest_framework import viewsets

class ProfileViewset(viewsets.ModelViewSet):
    "Viewsets for profiles."
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (ProfilePermission,)