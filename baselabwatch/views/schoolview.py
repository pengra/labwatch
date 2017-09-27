from baselabwatch.views import DashboardBase

class SchoolView(DashboardBase):
    template_name = 'base/schooladmin.html'
    current_app = 'baselabwatch'