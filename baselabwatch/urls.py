from django.conf.urls import url, include
from rest_framework import routers
from baselabwatch.api.profile import ProfileViewset

router = routers.DefaultRouter()
router.register(r'users', ProfileViewset)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework'))
]