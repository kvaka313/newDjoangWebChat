from django.forms import forms
from MyWebChat.models import Credential


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ['name', 'surname', 'login', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }