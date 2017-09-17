from baselabwatch.models import Subscription, School
from rest_framework import serializers


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for user."
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name='school-detail', queryset=School.objects.all())

    class Meta:
        model = Subscription
        fields = (
            'url',
            'school',
            'expires',
            'billing_cycle',
            'max_student_ids',
            'max_kiosks',
            'max_logs',
            'student_rewards',
            'data_intel',
            'precentage_discount',
            'numeric_discount'
        )