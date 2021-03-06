"""labwatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.contrib import admin
from labwatch import settings
from baselabwatch.views import IndexView, login_view, logout_view
import baselabwatch.urls
import logger.urls

# namespaces must match app names
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^staff/', admin.site.urls),
    url(r'^base/', include(baselabwatch.urls, namespace='baselabwatch')),
    url(r'^logger/', include(logger.urls, namespace='logger')),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
] 

if settings.DEBUG:
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
