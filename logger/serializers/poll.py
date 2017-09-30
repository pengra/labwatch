from django.contrib.auth.models import User
from rest_framework import serializers
from logger.models import PollQuestion, PollChoice
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(PollQuestion)

class PollQuestionSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for poll questions."
    class Meta:
        model = PollQuestion
        fields = (
            'pk',
            'question_text'
        )


class PollChoiceSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer of poll choices"
    question = serializers.HyperlinkedRelatedField(source="question.pk", view_name=resolution.resolve("pollquestion-detail"), queryset=PollQuestion.objects.all())

    class Meta:
        model = PollChoice
        fields = (
            'pk',
            'question',
            'choice_text',
            'votes'
        )
