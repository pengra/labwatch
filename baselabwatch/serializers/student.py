from baselabwatch.models import Student, School
from rest_framework import serializers
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(Student)

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for user."
    url = serializers.HyperlinkedIdentityField(view_name=resolution.resolve('student-detail'))
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name=resolution.resolve('school-detail'), read_only=True)

    class Meta:
        model = Student
        react_data = {
            'url': {},
            'student_id': {
                'label': 'Student ID',
                'help_text': 'This number must be unique.'
            },
            'first_name': {
                'label': 'Student First Name',
            },
            'last_name': {
                'label': 'Student Last Name',
                'help_text': 'If student has multiple last names, place all names here.'
            },
            'nick_name': {
                'label': 'Student "Nickname"',
                'help_text': 'An additional unique identifier for this student.',
                'placeholder': 'e.g. pengrnor000'
            },
            'teacher': {
                'help_text': 'Student\'s main teacher.'
            },
            'grade': {},
            'school': {},
            'email': {
                'label': 'Student email',
                'help_text': 'If student would like to recieve emails from LabWatch. We never give emails away to anyone.'
            },
            'signed_in': {},
        }
        fields = tuple(react_data.keys())
