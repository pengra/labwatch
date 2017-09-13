from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'dashboard/students/upload-spreadsheet/$', views.dashboard_student_bulk_view, name='dashboard-student-bulk'),
    url(r'dashboard/students/manage/$', views.dashboard_student_admin_view, name='dashboard-student'),
    url(r'dashboard/kiosk/$', views.DashboardKioskView.as_view(), name='dashboard-kiosk'),
    url(r'dashboard/poll/$', views.dashboard_poll_view, name='dashboard-poll'),
    url(r'dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/$', views.KioskView.as_view(), name='kiosk-page'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/poll/$', views.KioskPollView.as_view(), name='kiosk-poll'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/ping/$', views.kiosk_ping_json, name='kiosk-ping'),
    url(r'^$', views.CoverView.as_view(), name='index'),
]
