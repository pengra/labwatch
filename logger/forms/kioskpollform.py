from django import forms

class KioskForm(forms.Form):
    kiosk_pk = forms.IntegerField()
    name = forms.CharField()
    poll_question = forms.CharField(required=False)
    poll_choices = forms.CharField(required=False)
    