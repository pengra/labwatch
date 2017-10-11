from django import forms
from django.core.exceptions import ValidationError
from logger.models.session import INPUT_MODE

class LogForm(forms.Form):
    pk = forms.IntegerField()
    query_input = forms.CharField()
    poll_result = forms.CharField(required=False)

    @property
    def mode(self):
        if self.is_valid():
            query = self.cleaned_data['query_input']
            if query.lower() == 'vote':
                return 'VOTE' # this is a vote
            elif query.isdigit():
                return INPUT_MODE[0][0] # studentID
            elif '@' in query and '.' in query:
                return INPUT_MODE[2][0] # email
            elif len(query.split(' ')) >= 2:
                return INPUT_MODE[1][0] # name
            else:
                return INPUT_MODE[3][0] # nickname
