from django.shortcuts import render
from django.template.backends import django
from django.views.generic import FormView

from MyWebChat.forms import RegistrationForm, LoginForm
from MyWebChat.models import Bans


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return render(request, 'index.html', {})
        return render(request, 'registration.html', {'error': 'error in registration', 'form': RegistrationForm})

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        ulogin = request.session.get('user_login')
        role = request.session.get('role')
        if ulogin is not None:
            if role is not None and role == 'admin':
                return render(request, 'admin.html', {'user': ulogin})
            #select * from bans join credetials on id = id_user Where credentials.login=ulogin
            ban = Bans.objects.filter(id_user__login=ulogin).first()
            if ban is None:
                return render(request, 'chat.html', {'user': ulogin})
            else:
                return render(request, 'ban.html', {'user': ulogin})
        else:
            form = self.get_form(LoginView.form_class)
            return render(request, LoginView.template_name, {'form': form})
