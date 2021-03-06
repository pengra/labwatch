from baselabwatch.models import Student
from baselabwatch.serializers import StudentSerializer
from rest_framework import viewsets
from baselabwatch.permissions import StudentPermission
from rest_framework.filters import SearchFilter

class StudentViewSet(viewsets.ModelViewSet):
    "Viewsets for Students."
    # queryset = Student.objects.all
    serializer_class = StudentSerializer
    permission_classes = (StudentPermission,)
    filter_backends = (SearchFilter, )
    search_fields = (
        '^first_name', '^last_name', 'last_name', '=nick_name',
        '=student_id', '=email',
    )

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile.school)

    def get_queryset(self):
        if self.request.user and self.request.user.profile.school:
            queryset = self.request.user.profile.school.student_set.all()
        else:
            queryset = []
        return queryset
