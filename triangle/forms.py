from django import forms

from triangle.models import Person


class GetForm(forms.Form):
    catet1 = forms.IntegerField(label='Катет 1', required=True, min_value=1)
    catet2 = forms.IntegerField(label='Катет 2', required=True, min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
