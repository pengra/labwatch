"Various forms that aren't covered by serializers"

from django import forms


class XMLFileUploadForm(forms.Form):
    "Form for batch student XML uploads."
    spreadsheet = forms.FileField()
    dupe_action = forms.CharField()