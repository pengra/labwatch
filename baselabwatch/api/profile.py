from django.contrib.auth.models import User
from baselabwatch.serializers.user import ProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class ProfileViewset(viewsets.ModelViewSet):
    "Viewsets for profiles."
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser,)
