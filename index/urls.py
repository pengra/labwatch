from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'login/$', views.login_view, name='login'),
    url(r'dashboard/kiosk/$', views.dashboard_kiosk_view, name='dashboard-kiosk'),
    url(r'dashboard/$', views.dashboard_view, name='dashboard'),
    url(r'kiosk/(?P<auth_code>[a-zA-Z0-9]+)/$', views.kiosk_view, name='kiosk-page'),
    url(r'^$', views.cover_view, name='index'),
]
