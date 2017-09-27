from baselabwatch.views import DashboardBase

class ProfileView(DashboardBase):
    template_name = 'base/profileadmin.html'
    current_app = 'baselabwatch'