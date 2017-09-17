from baselabwatch.models import Student, School
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for user."
    school = serializers.HyperlinkedRelatedField(source="school.pk", view_name='school-detail', queryset=School.objects.all())

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
