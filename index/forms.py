from django import forms


class KioskForm(forms.Form):
    "A form for /dashboard/kiosk/ editing"
    name = forms.CharField()
    school = forms.CharField()
    active = forms.CharField()
    auth_code = forms.CharField()
    pk = forms.IntegerField()
    proxy_method = forms.CharField(required=False)


class LoginForm(forms.Form):
    "A form for an AJAX hit from a kiosk."
    mode = forms.CharField()
    return_value = forms.CharField()

    def is_valid_card_number(self):
        "Is this a card number the user just typed in?"
        is_valid = self.is_valid()
        is_box = self.cleaned_data['mode'] == '_box'
        is_numeric = self.cleaned_data['return_value'].isdigit()
        return is_valid and is_box and is_numeric

    def is_valid_email(self):
        "Is this an email this person just typed in?"
        is_valid = self.is_valid()
        is_box = self.cleaned_data['mode'] == '_box'
        contains_at = "@" in self.cleaned_data['return_value']
        contains_period = '.' in self.cleaned_data['return_value']
        return is_valid and is_box and contains_at and contains_period

    def is_valid_name(self):
        "Is this a valid name this person just typed in?"
        is_valid = self.is_valid()
        is_box = self.cleaned_data['mode'] == '_box'
        is_text = self.cleaned_data['return_value'].replace(' ', '').replace('-', '').isalpha()
        is_one_space_min = len(self.cleaned_data['return_value'].split(' ')) > 1
        return is_valid and is_box and is_text and is_one_space_min
