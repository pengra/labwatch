from django.contrib.auth.models import User
import django.forms
from rest_framework import serializers
from baselabwatch.models import School
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(School)


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name=resolution.resolve('school-detail'), read_only=True)
    primary_contact = serializers.HyperlinkedRelatedField(
        source='primary_contact.pk',
        view_name=resolution.resolve('user-detail'),
        read_only=True)
    name = serializers.CharField(label='School Name', help_text='Your school\'s full name', style={'placeholder': 'e.g. Edmonds Woodway High School'})
    short_name = serializers.CharField(label='School Abbreviation', help_text='A short name for your school.', style={'placeholder': 'e.g. EWHS'})
    auth_code = serializers.CharField(label='School Code', help_text='A code for letting other teachers join.', read_only=True)
    school_image = serializers.CharField(label='School Logo', help_text='A link to a school image.')

    class Meta:
        model = School
        fields = (
            'url',
            'name',
            'short_name',
            'primary_contact',
            'auth_code',
            'school_image'
        )
