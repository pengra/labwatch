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
        fields = (
            'url',
            'student_id',
            'first_name',
            'last_name',
            'nick_name',
            'teacher',
            'grade',
            'school',
            'email',
            'signed_in',
        )
