from django import forms

class LogForm(forms.Form):
    student_input = forms.CharField()
    poll_result = forms.CharField()

    def is_valid_card_number(self):
        "Is this a card number the user just typed in?"
        is_valid = self.is_valid()
        is_numeric = self.cleaned_data['student_input'].isdigit()
        return is_valid and is_numeric

    def is_valid_email(self):
        "Is this an email this person just typed in?"
        is_valid = self.is_valid()
        contains_at = "@" in self.cleaned_data['student_input']
        contains_period = '.' in self.cleaned_data['student_input']
        return is_valid and contains_at and contains_period

    def is_valid_name(self):
        "Is this a valid name this person just typed in?"
        is_one_space_min = len(self.cleaned_data['student_input'].split(' ')) > 1
        return self.is_valid_nickname() and is_one_space_min

    def is_valid_nickname(self):
        "is this a valid nickname this person just yped in?"
        is_valid = self.is_valid()
        is_text = self.cleaned_data['student_input'].replace(' ', '').replace('-', '').isalpha()
        return is_valid and is_text

    def is_valid_poll(self):
        "Is this a valid poll option coming through?"
        is_valid = self.is_valid()
        return is_valid
