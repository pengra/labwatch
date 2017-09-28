from django.conf.urls import url, include
from rest_framework import routers
from baselabwatch import api
from baselabwatch import views


router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'profiles', api.ProfileViewSet)
router.register(r'schools', api.SchoolViewSet)
router.register(r'students', api.StudentViewSet, base_name='student')
router.register(r'subscriptions', api.SubscriptionViewSet)
router.register(r'reports', api.UserReportViewSet)


urlpatterns = [
    url(r'^$', views.SchoolView.as_view(), name='index'),
    url(r'^student/$', views.StudentView.as_view(), name='student'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^api/v1/', include(router.urls, namespace='api')),
    url(r'^api/v1/upload/$', views.XMLUploadView.as_view(), name='student-upload'),
]