from django.contrib.auth.models import User
from baselabwatch.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import JSONRenderer

class UserViewSet(viewsets.ModelViewSet):
    "Viewsets for Users."
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    renderer_classes = [JSONRenderer]
