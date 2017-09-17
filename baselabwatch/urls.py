from django.conf.urls import url, include
from rest_framework import routers
from baselabwatch import api

router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'profiles', api.ProfileViewSet)
router.register(r'schools', api.SchoolViewSet)
router.register(r'students', api.StudentViewSet)
router.register(r'subscriptions', api.SubscriptionViewSet)
router.register(r'reports', api.UserReportViewSet)


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework'))
]