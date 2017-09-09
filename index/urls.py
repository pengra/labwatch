from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'login/$', views.login_view, name='login'),
    url(r'dashboard/kiosk/$', views.dashboard_kiosk_view, name='dashboard-kiosk'),
    url(r'dashboard/$', views.dashboard_view, name='dashboard'),
    url(r'$', views.cover_view, name='index'),
]
