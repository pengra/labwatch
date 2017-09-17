from django.contrib.auth.models import User
from rest_framework import serializers
from baselabwatch.models import School

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    primary_contact = serializers.HyperlinkedRelatedField(
        source='primary_contact.pk', 
        view_name='user-detail', 
        queryset=User.objects.all())

    class Meta:
        model = School
        fields = (
            'name',
            'primary_contact',
            'auth_code',
            'school_image'
        )