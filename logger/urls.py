from django.conf.urls import include, url
from rest_framework import routers

from logger import api, views

router = routers.DefaultRouter()
router.register(r'sessions', api.StudentSessionViewSet, base_name='session')
router.register(r'kiosks', api.KioskViewSet, base_name='kiosk')
router.register(r'poll-questions', api.PollQuestionViewSet)
router.register(r'poll-choices', api.PollChoiceViewSet)
router.register(r'imagecards', api.ImageCardViewSet)


urlpatterns = [
    url(r'^$', views.OverviewView.as_view(), name='index'),
    url(r'^kiosk/$', views.KioskView.as_view(), name='kiosk'),
    url(r'^k/$', views.ClientView.as_view(), name='client'),
    url(r'^k/(?P<uuid>[0-9a-f -]{36})/$', views.ClientView.as_view(), name='client'),
    url(r'^api/v1/', include(router.urls, namespace='api')),
    url(r'^api/v1/export/$', views.ReportExportView.as_view(), name='export'),
]
