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
            'name': {
                'placeholder': 'e.g. EWHS',
                'label': 'School Name',
                'help_text': 'An abbreviation of your school\'s name'
            },
            'primary_contact': {
                # 'display': '{primary_contact.first_name} {primary_contact.last_name}: {primary_contact.email}',
                'read_only': True
            },
            'auth_code': {
                'label': 'School code',
                'read_only': True,
                'help_text': 'Give this code to teachers who\'d like to join LabWatch.'
            },
            'school_image': {
                'placeholder': 'e.g. an imgur link such as https://imgur.com/XrHBZbV.png',
                'help_text': 'Your school logo. Upload the image to another website and paste the link here.'
            },
        }
        fields = tuple(react_data.keys())
