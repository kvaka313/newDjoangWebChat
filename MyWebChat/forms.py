from django.forms import ModelForm, PasswordInput, CharField, Form

from MyWebChat.models import Credential


class RegistrationForm(ModelForm):
    class Meta:
        model = Credential
        fields = ['name', 'login', 'password']
        widgets = {
            'password': PasswordInput(),
        }

class LoginForm(Form):
    login = CharField(max_length=Credential.max_len_cred, label='Login')
    password = CharField(max_length=Credential.max_len_cred, widget=PasswordInput)