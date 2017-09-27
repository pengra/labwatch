from baselabwatch.models import Student
from baselabwatch.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter

class StudentViewSet(viewsets.ModelViewSet):
    "Viewsets for Students."
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (SearchFilter, )
    search_fields = (
        'first_name', 'last_name', 'nick_name',
        'student_id', 'teacher', 'grade',
        'email',
    )

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile.school)
            

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)