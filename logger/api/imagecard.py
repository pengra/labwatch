from logger.models import ImageCard
from logger.serializers import ImageCardSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from random import choice

class ImageCardViewSet(viewsets.ModelViewSet):
    "Viewsets for Image cards."
    serializer_class = ImageCardSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self, *args, **kwargs):
        random = self.request.query_params.get('random')
        query = ImageCard.objects.filter(school=self.request.user.profile.school)
        if random:
            return [choice(query)]
        return query
        