from rest_framework import serializers
from baselabwatch.models import Student
from logger.models import StudentSession

class StudentSessionSerializer(serializers.HyperlinkedModelSerializer):
    "Serializer for profile."
    student = serializers.HyperlinkedRelatedField(source="student.pk", view_name='student-detail', queryset=Student.objects.all())

    class Meta:
        model = StudentSession
        fields = (
            'url',
            'student',
            'sign_in_mode',
            'sign_in_timestamp',
            'sign_out_mode',
            'sign_out_timestamp',
        )
