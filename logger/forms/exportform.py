from django import forms

class ExportForm(forms.Form):
    in_method = forms.BooleanField(required=False)
    in_column = forms.BooleanField(required=False)
    out = forms.BooleanField(required=False)
    out_method = forms.BooleanField(required=False)
    grade = forms.BooleanField(required=False)
    names = forms.BooleanField(required=False)
    teachers = forms.BooleanField(required=False)
    id_column = forms.BooleanField(required=False)
    target = forms.CharField()

    