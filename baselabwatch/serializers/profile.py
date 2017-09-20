from django.contrib.auth.models import User
from rest_framework import serializers
from baselabwatch.models import Profile, School
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(Profile)

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    url = serializers.HyperlinkedIdentityField(view_name=resolution.resolve("profile-detail"))
    user = serializers.HyperlinkedRelatedField(source="user.pk", view_name=resolution.resolve('user-detail'), queryset=User.objects.all())
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name='school-detail', queryset=School.objects.all())

    class Meta:
        model = Profile
        fields = (
            'url',
            'user',
            'school',
            'engineer',
            'librarian',
            'techsavy',
            'beta_tester'
        )
        