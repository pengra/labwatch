from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'login/$', views.login_view, name='login'),
    url(r'$', views.cover_view, name='index'),
]
