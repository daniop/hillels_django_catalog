from django import forms


class GetForm(forms.Form):
    catet1 = forms.IntegerField(label='Катет 1', required=True, min_value=1)
    catet2 = forms.IntegerField(label='Катет 2', required=True, min_value=1)
