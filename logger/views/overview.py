from baselabwatch.views import DashboardBase

class OverviewView(DashboardBase):
    template_name = "logger/overview.html"
    current_app = "logger"
