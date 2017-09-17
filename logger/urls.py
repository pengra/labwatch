from django.conf.urls import url, include
from rest_framework import routers
from logger import api

router = routers.DefaultRouter()
router.register(r'sessions', api.StudentSessionViewSet)
router.register(r'kiosks', api.KioskViewSet)
router.register(r'poll-questions', api.PollQuestionViewSet)
router.register(r'poll-choices', api.PollChoiceViewSet)
router.register(r'imagecards', api.ImageCardViewSet)


urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]