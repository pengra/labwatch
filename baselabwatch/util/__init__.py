from labwatch.settings import LABWATCH_APPS
import importlib


def get_title_links():
    "Function that grabs all the title links."
    links = []
    for app in LABWATCH_APPS:
        app = importlib.import_module("{}.apps".format(app))
        links.append(app.ReactConfig.tab_title)
        # Faster with del
        # Intel i7 timeit tests
        del app
    return links
