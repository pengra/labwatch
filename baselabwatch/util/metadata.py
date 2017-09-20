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
        meta_data = super().get_serializer_info(serializer)
        # meta_data['hi'] = True (places it on the outside )
        return meta_data


    def get_field_info(self, field):
        field_info = super().get_field_info(field)
        field_info['hi'] = True
        return field_info
