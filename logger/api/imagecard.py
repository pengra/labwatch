from logger.models import ImageCard
from logger.serializers import ImageCardSerializer
from rest_framework import viewsets
from logger.permissions import ImageCardPermission
from random import choice

class ImageCardViewSet(viewsets.ModelViewSet):
    "Viewsets for Image cards."
    serializer_class = ImageCardSerializer
    permission_classes = (ImageCardPermission,)

    def get_queryset(self, *args, **kwargs):
        random = self.request.query_params.get('random')
        query = ImageCard.objects.filter(school=self.request.user.profile.school)
        if random and query:
            return [choice(query)]
        return query
        