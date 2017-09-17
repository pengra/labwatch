from rest_framework import serializers
from baselabwatch.models import School
from logger.models import ImageCard

class ImageCardSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name='school-detail', queryset=School.objects.all())

    class Meta:
        model = ImageCard
        fields = (
            'url',
            'school',
            'image',
            'source'
        )
