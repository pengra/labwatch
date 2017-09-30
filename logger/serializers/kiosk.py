from rest_framework import serializers
from baselabwatch.models import School
from logger.models import Kiosk, PollQuestion, PollChoice
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(School)
resolution2 = URLResolution(Kiosk)


class KioskSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    school = serializers.HyperlinkedRelatedField(
        source="school.pk", view_name=resolution.resolve('school-detail'), read_only=True)
    name = serializers.CharField(help_text="Kiosk Title")
    auth_code = serializers.CharField(
        label="Kiosk Code", help_text="A code for quick kiosk access", read_only=True)
    poll_pk = serializers.HyperlinkedRelatedField(
        source='poll.pk', view_name=resolution2.resolve('pollquestion-detail'), read_only=True)
    poll_question = serializers.CharField(
        source='poll.question_text', label="Poll Question", read_only=True)
    tb_formatted_pollchoices = serializers.SerializerMethodField(read_only=True)
    # PrimaryKeyRelatedField(source="poll.pollchoice_set", many=True, queryset=PollChoice.objects.all())


    def get_tb_formatted_pollchoices(self, kiosk):
        if kiosk.poll:
            return "\n".join((str(choice) for choice in kiosk.poll.pollchoice_set.all()))
        return ""

    class Meta:
        model = Kiosk
        fields = (
            'pk',
            'name',
            'school',
            'auth_code',
            'poll_pk',
            'poll_question',
            'tb_formatted_pollchoices'
        )
