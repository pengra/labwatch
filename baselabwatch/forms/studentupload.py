"Various forms that aren't covered by serializers"

from django import forms


class XMLFileUploadForm(forms.Form):
    "Form for batch student XML uploads."
    spreadsheet = forms.FileField()
    dupe_action = forms.CharField()
    studentid = forms.CharField()
    fname = forms.CharField()
    lname = forms.CharField()
    grade = forms.CharField(required=False)
    teacher = forms.CharField(required=False)
    nickname = forms.CharField(required=False)
    email = forms.CharField(required=False)