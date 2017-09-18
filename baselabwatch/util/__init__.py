from labwatch.settings import LABWATCH_APPS
from django.urls import reverse
from django.core.urlresolvers import NoReverseMatch
import importlib


def get_app_metadata():
    "Function that grabs all the title links."
    meta_data = []
    for app in LABWATCH_APPS:
        app_module = importlib.import_module("{}.apps".format(app))
        try:
            url = reverse("{}:index".format(app))
        except NoReverseMatch:
            url = '#'
        meta_data.append({
            "title": app_module.ReactConfig.tab_title,
            "name": app,
            "url": url,
        })
        # Faster with del
        # Intel i7 timeit tests
        del app
    return meta_data
