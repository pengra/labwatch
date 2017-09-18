from baselabwatch.views import DashboardBase

class LogDashView(DashboardBase):
    template_name = "base/_base.html"
    current_app = "logger"