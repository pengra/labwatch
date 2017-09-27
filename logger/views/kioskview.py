from baselabwatch.views import DashboardBase

class KioskView(DashboardBase):
    template_name = "logger/kioskview.html"
    current_app = "logger"
