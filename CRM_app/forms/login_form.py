from django import forms
from CRM_app.models import New

class UserForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['name', 'password']
        