from django.contrib.auth.models import User
from rest_framework import serializers
from baselabwatch.models import School
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(School)


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    primary_contact = serializers.HyperlinkedRelatedField(
        source='primary_contact.pk',
        view_name=resolution.resolve('user-detail'),
        read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name=resolution.resolve('school-detail'), read_only=True)

    class Meta:
        model = School
        react_data = {
            'url': {
                'hidden': True
            },
            'name': {},
            'primary_contact': {
                'display': '{primary_contact.first_name} {primary_contact.last_name}: {primary_contact.email}',
                'read_only': True
            },
            'auth_code': {},
            'school_image': {},
        }
        fields = tuple(react_data.keys())
