from django.contrib.auth.models import User
from rest_framework import serializers
from logger.models import PollQuestion, PollChoice

class PollQuestionSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for poll questions."
    class Meta:
        model = PollQuestion
        fields = (
            'url',
            'question_text'
        )


class PollChoiceSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer of poll choices"
    question = serializers.HyperlinkedRelatedField(source="question.pk", view_name="pollquestion-detail", queryset=PollQuestion.objects.all())

    class Meta:
        model = PollChoice
        fields = (
            'url',
            'question',
            'choice_text',
            'votes'
        )