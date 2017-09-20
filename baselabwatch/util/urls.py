"""
utilities regarding urls/reverse/resolution go here
"""
class URLResolution:
    "Get a namespace to resolve when given a model and subnamespace. Usable for all serializers"

    def __init__(self, model=None, subnamespace='api'):
        self.namespaces = [
            model._meta.app_label,
            subnamespace
        ]

    def resolve(self, view_name):
        "Only need view_name to get resolution in the format of: appname:subnamespce:view_name"
        return ":".join(self.namespaces) + ":" + view_name
