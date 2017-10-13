from rest_framework import serializers
from baselabwatch.models import School
from logger.models import ImageCard
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(School)

class ImageCardSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    school = serializers.HyperlinkedRelatedField(
        source="school.pk", 
        view_name=resolution.resolve('school-detail'),
        queryset=School.objects.all()
    )

    class Meta:
        model = ImageCard
        fields = (
            'school',
            'image',
            'source'
        )
