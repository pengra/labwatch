from logger.models import StudentSession
from logger.serializers import StudentSessionSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

class StudentSessionViewSet(viewsets.ModelViewSet):
    "Viewsets for Users."
    queryset = StudentSession.objects.all()
    serializer_class = StudentSessionSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = StudentSession.objects.filter(student__school=self.request.user.profile.school)
        if self.request.query_params.get('signed_in', False):
            queryset = queryset.filter(sign_out_mode='', sign_out_timestamp=None)
        elif self.request.query_params.get('signed_out', False):
            queryset = queryset.exclude(sign_out_mode='', sign_out_timestamp=None)
        return queryset
