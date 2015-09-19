from django import forms

class SendMoneyForm(forms.Form):
    recipient_email = forms.EmailField()
    dollars = forms.FloatField(min_value=0.01)
