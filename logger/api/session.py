from django.db.models import Q
from logger.models import StudentSession
from logger.serializers import StudentSessionSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter


class StudentSessionViewSet(viewsets.ModelViewSet):
    "Viewsets for Users."
    queryset = StudentSession.objects.all()
    serializer_class = StudentSessionSerializer
    permission_classes = (IsAdminUser,)
    
    def get_queryset(self):
        queryset = StudentSession.objects.filter(
            student__school=self.request.user.profile.school)

        # Dummy search because foreign key searches don't work
        search = self.request.query_params.get('search')
        if search:
            query = (
                Q(student__first_name__icontains=search)
                | Q(student__last_name__icontains=search)
                | Q(student__nick_name__icontains=search)
                | Q(student__email__icontains=search)
                | Q(student__student_id__icontains=search)
            )
            
            queryset = queryset.filter(query)

        # Queries for getting ONLY signedin/signedout students
        if self.request.query_params.get('signed_in', False):
            queryset = queryset.filter(
                sign_out_mode='', sign_out_timestamp=None)
        elif self.request.query_params.get('signed_out', False):
            queryset = queryset.exclude(
                sign_out_mode='', sign_out_timestamp=None)

        # Queries for filtering by dates

        mode = self.request.query_params.get('mode', 'all')

        if self.request.query_params.get('time_gte') and self.request.query_params.get('regard_gte'):
            time_gte = self.request.query_params.get('time_gte')
            if mode == 'all':
                queryset = queryset.filter(
                    Q(sign_in_timestamp__gte=time_gte)
                    | Q(sign_out_timestamp__gte=time_gte)
                )
            elif mode == 'in':
                queryset = queryset.filter(Q(sign_in_timestamp__gte=time_gte))
            elif mode == 'out':
                queryset = queryset.filter(Q(sign_out_timestamp__gte=time_gte))

        if self.request.query_params.get('time_lte') and self.request.query_params.get('regard_lte'):
            time_lte = self.request.query_params.get('time_lte')
            if mode == 'all':
                queryset = queryset.filter(
                    Q(sign_in_timestamp__lte=time_lte)
                    | Q(sign_out_timestamp__lte=time_lte)
                )
            elif mode == 'in':
                queryset = queryset.filter(Q(sign_in_timestamp__lte=time_lte))
            elif mode == 'out':
                queryset = queryset.filter(Q(sign_out_timestamp__lte=time_lte))

        return queryset
