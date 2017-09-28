from rest_framework import serializers
from baselabwatch.models import Student
from logger.models import StudentSession
from baselabwatch.util.urls import URLResolution

resolution = URLResolution(StudentSession)
resolution2 = URLResolution(Student)

class StudentSessionSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    url = serializers.HyperlinkedIdentityField(view_name=resolution.resolve('session-detail'))
    student = serializers.HyperlinkedRelatedField(source="student.pk", view_name=resolution2.resolve('student-detail'), queryset=Student.objects.all())

    student_id = serializers.IntegerField(source='student.student_id', read_only=True)
    first_name = serializers.CharField(source='student.first_name', read_only=True)
    last_name = serializers.CharField(source='student.last_name', read_only=True)
    teacher = serializers.CharField(source='student.teacher', read_only=True)
    grade = serializers.CharField(source='student.grade', read_only=True)

    class Meta:
        model = StudentSession
        fields = (
            'url',
            'student',
            'student_id',
            'first_name',
            'last_name',
            'teacher',
            'grade',
            'sign_in_mode',
            'sign_in_timestamp',
            'sign_out_mode',
            'sign_out_timestamp',
        )
