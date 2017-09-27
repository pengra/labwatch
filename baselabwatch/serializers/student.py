from baselabwatch.models import Student, School
from rest_framework import serializers
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(Student)

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for user."
    url = serializers.HyperlinkedIdentityField(view_name=resolution.resolve('student-detail'))
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name=resolution.resolve('school-detail'), read_only=True)
    signed_in = serializers.BooleanField(read_only=True)
    student_id = serializers.CharField(label='Student ID', help_text='This number must be unique.')
    nick_name = serializers.CharField(help_text='Should the user forget his/her ID, they can alternatively type in a username or nickname.', style={'placeholder': 'e.g. pengrnor000'})

    class Meta:
        model = Student
        fields = (
            'url',
            'pk',
            'student_id',
            'first_name',
            'last_name',
            'nick_name',
            'email',
            'teacher',
            'grade',
            'school',
            'signed_in',
        )
