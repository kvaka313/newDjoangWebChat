from django.forms import ModelForm, PasswordInput

from MyWebChat.models import Credential


class RegistrationForm(ModelForm):
    class Meta:
        model = Credential
        fields = ['name', 'login', 'password']
        widgets = {
            'password': PasswordInput(),
        }