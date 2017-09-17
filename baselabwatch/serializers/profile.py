from django.contrib.auth.models import User
from rest_framework import serializers
from baselabwatch.models import Profile, School

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    user = serializers.HyperlinkedRelatedField(source="user.pk", view_name='user-detail', queryset=User.objects.all())
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
