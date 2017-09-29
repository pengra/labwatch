from django.contrib.auth.models import User
from rest_framework import serializers
from baselabwatch.models import Profile, School
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(Profile)

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    url = serializers.HyperlinkedIdentityField(view_name=resolution.resolve("profile-detail"))
    user = serializers.HyperlinkedRelatedField(source="user.pk", view_name=resolution.resolve('user-detail'), read_only=True)
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name=resolution.resolve('school-detail'), read_only=True)
    engineer = serializers.BooleanField(read_only=True)
    librarian = serializers.BooleanField(read_only=True)
    techsavy = serializers.BooleanField(read_only=True)


    class Meta:
        model = Profile
        fields = (
            'url',
            'user',
            'school',
            'engineer',
            'librarian',
            'techsavy',
            'beta_tester',
            'timezone'
        )
        
        