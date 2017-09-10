from django import forms

class KioskForm(forms.Form):
    "A form for /dashboard/kiosk/ editing"
    name = forms.CharField()
    school = forms.CharField()
    active = forms.CharField()
    auth_code = forms.CharField()
    pk = forms.IntegerField()
    proxy_method = forms.CharField(required=False)
    