from django.contrib.auth.models import User
from rest_framework import serializers
from baselabwatch.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for user."
    profile = serializers.HyperlinkedRelatedField(source="profile.pk", view_name='profile-detail', queryset=Profile.objects.all())

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'email',
            'is_staff',
            'profile',
        )
