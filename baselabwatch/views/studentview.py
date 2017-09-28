from baselabwatch.views import DashboardBase
from baselabwatch.serializers import StudentSerializer

class StudentView(DashboardBase):
    template_name = 'base/studentadmin.html'
    current_app = 'baselabwatch'
    serializer = StudentSerializer
