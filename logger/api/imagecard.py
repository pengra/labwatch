from logger.models import ImageCard
from logger.serializers import ImageCardSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class ImageCardViewSet(viewsets.ModelViewSet):
    "Viewsets for Image cards."
    queryset = ImageCard.objects.all()
    serializer_class = ImageCardSerializer
    permission_classes = (IsAdminUser,)
