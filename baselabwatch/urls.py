from django.conf.urls import url, include
from rest_framework import routers
from baselabwatch import api
from baselabwatch import views


router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'profiles', api.ProfileViewSet)
router.register(r'schools', api.SchoolViewSet)
router.register(r'students', api.StudentViewSet)
router.register(r'subscriptions', api.SubscriptionViewSet)
router.register(r'reports', api.UserReportViewSet)


urlpatterns = [
    url(r'$', views.DashboardBase.as_view(), name='index'),
    url(r'^api/v1/', include(router.urls, namespace='api')),

]