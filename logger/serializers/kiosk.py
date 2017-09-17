from rest_framework import serializers
from baselabwatch.models import School
from logger.models import Kiosk, PollQuestion

class KioskSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name='school-detail', queryset=School.objects.all())
    poll = serializers.HyperlinkedRelatedField(source='poll.pk', view_name='pollquestion-detail', queryset=PollQuestion.objects.all())

    class Meta:
        model = Kiosk
        fields = (
            'url',
            'name',
            'school',
            'auth_code',
            'active',
            'poll'
        )
