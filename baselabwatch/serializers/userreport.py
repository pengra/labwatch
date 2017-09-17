from django.contrib.auth.models import User
from baselabwatch.models import UserReport
from rest_framework import serializers


class UserReportSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for user reports."
    user = serializers.HyperlinkedRelatedField(source="user.pk", view_name='user-detail', queryset=User.objects.all())

    class Meta:
        model = UserReport
        fields = (
            'url',
            'report_type',
            'title',
            'content',
            'dealt_with',
            'user'
        )
