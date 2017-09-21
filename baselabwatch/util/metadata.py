from labwatch.settings import DEBUG
from rest_framework import serializers
from rest_framework.metadata import (
    SimpleMetadata, ClassLookupDict,
    clone_request, exceptions,
    PermissionDenied, Http404,
    OrderedDict, force_text
)

class ReactMetadata(SimpleMetadata):
    """
    Grab react data and pass it through the OPTIONS view
    """
    label_lookup = ClassLookupDict({
        serializers.Field: 'text',
        serializers.BooleanField: 'checkbox',
        serializers.NullBooleanField: 'checkbox',
        serializers.CharField: 'text',
        serializers.URLField: 'url',
        serializers.EmailField: 'email',
        serializers.RegexField: 'text',
        serializers.SlugField: 'text',
        serializers.IntegerField: 'number',
        serializers.FloatField: 'number',
        serializers.DecimalField: 'number',
        serializers.DateField: 'date',
        serializers.DateTimeField: 'datetime-local',
        serializers.TimeField: 'time',
        serializers.ChoiceField: 'select',
        serializers.MultipleChoiceField: 'select',
        serializers.FileField: 'file',
        serializers.ImageField: 'image',
        serializers.ListField: 'list',
        serializers.DictField: 'nested object',
        serializers.Serializer: 'nested object',
    })

    def get_serializer_info(self, serializer):
        """
        Given an instance of a serializer, return a dictionary of metadata
        about its fields.
        """
        if hasattr(serializer, 'child'):
            # If this is a `ListSerializer` then we want to examine the
            # underlying child serializer instance instead.
            serializer = serializer.child
        meta_data = OrderedDict([
            (field_name, self.get_field_info(field, field_name))
            for field_name, field in serializer.fields.items()
        ])
        meta_data['_debug'] = DEBUG
        return meta_data


    def get_field_info(self, field, field_name):
        # need to get what field name this is
        field_info = super().get_field_info(field)
        field_info['react_meta'] = field.parent.Meta.react_data[field_name]
        return field_info
