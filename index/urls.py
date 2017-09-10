from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'login/$', views.login_view, name='login'),
    url(r'dashboard/kiosk/$', views.dashboard_kiosk_view, name='dashboard-kiosk'),
    url(r'dashboard/poll/$', views.dashboard_poll_view, name='dashboard-poll'),
    url(r'dashboard/$', views.dashboard_view, name='dashboard'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/$', views.kiosk_view, name='kiosk-page'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/poll/$', views.kiosk_poll_view, name='kiosk-poll'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/ping/$', views.kiosk_ping_json, name='kiosk-ping'),
    url(r'^$', views.cover_view, name='index'),
]
