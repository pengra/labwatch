from rest_framework import serializers
from baselabwatch.models import School
from logger.models import Kiosk, PollQuestion
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(School)
resolution2 = URLResolution(Kiosk)

class KioskSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name=resolution.resolve('school-detail'), read_only=True)
    poll = serializers.HyperlinkedRelatedField(source='poll.pk', view_name=resolution2.resolve('pollquestion-detail'), read_only=True)
    name = serializers.CharField(help_text="Kiosk Title")
    auth_code = serializers.CharField(label="Kiosk Code", help_text="A code for quick kiosk access", read_only=True)

    class Meta:
        model = Kiosk
        fields = (
            'pk',
            'name',
            'school',
            'auth_code',
            'poll',
        )
