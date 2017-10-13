from logger.models import Kiosk
from logger.serializers import KioskSerializer
from rest_framework import viewsets
from logger.permissions import KioskPermission


class KioskViewSet(viewsets.ModelViewSet):
    "Viewsets for Users."
    serializer_class = KioskSerializer
    permission_classes = (KioskPermission,)

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile.school)

    def get_queryset(self, *args, **kwargs):
        return Kiosk.objects.filter(school=self.request.user.profile.school)
