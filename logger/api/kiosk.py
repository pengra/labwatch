from logger.models import Kiosk
from logger.serializers import KioskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class KioskViewSet(viewsets.ModelViewSet):
    "Viewsets for Users."
    queryset = Kiosk.objects.all()
    serializer_class = KioskSerializer
    permission_classes = (IsAdminUser,)
