from django.contrib.auth.models import User
from baselabwatch.serializers import UserSerializer
from rest_framework import viewsets
from baselabwatch.permissions import UserPermission
from rest_framework.renderers import JSONRenderer

class UserViewSet(viewsets.ModelViewSet):
    "Viewsets for Users."
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission, )
    # renderer_classes = [JSONRenderer]
