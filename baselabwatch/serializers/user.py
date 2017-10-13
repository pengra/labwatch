from django.contrib.auth.models import User
from rest_framework import serializers
from baselabwatch.models import Profile
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(Profile)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for user."
    url = serializers.HyperlinkedIdentityField(view_name=resolution.resolve('user-detail'))
    profile = serializers.HyperlinkedRelatedField(source="profile.pk", view_name=resolution.resolve('profile-detail'), read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'email',
            'is_staff',
            'profile',
        )
