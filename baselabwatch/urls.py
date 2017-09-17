from django.conf.urls import url, include
from rest_framework import routers
from baselabwatch.api import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework'))
]