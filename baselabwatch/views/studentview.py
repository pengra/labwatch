from baselabwatch.views import DashboardBase

class StudentView(DashboardBase):
    template_name = 'base/studentadmin.html'
    current_app = 'baselabwatch'