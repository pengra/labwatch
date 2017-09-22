from baselabwatch.models import Subscription
from baselabwatch.serializers import SubscriptionSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import JSONRenderer

class SubscriptionViewSet(viewsets.ModelViewSet):
    "Viewsets for User reports."
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAdminUser,)
    # renderer_classes = [JSONRenderer]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile.school)
