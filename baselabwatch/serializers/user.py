from django.contrib.auth.models import User
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    class Meta:
        model = User
        fields = (
            'url', 
            'username', 
            'email', 
            'is_staff',
            'profile.school',
            'profile.engineer',
            'profile.librarian',
            'profile.tech_savy',
            'profile.beta_tester'
        )