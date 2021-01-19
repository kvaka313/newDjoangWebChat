from django.shortcuts import render
from django.template.backends import django
from django.views.generic import FormView

from MyWebChat.forms import RegistrationForm, LoginForm
from MyWebChat.models import Bans, Credential


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
                return render(request, 'ban.html', {'login': ulogin})
        else:
            form = self.get_form(LoginView.form_class)
            return render(request, LoginView.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_login = login_form.cleaned_data['login']
            user_password = login_form.cleaned_data['password']
            c = Credential.objects.filter(login=user_login, password=user_password).first()
            if c is not None:
                request.session['user_login'] = user_login
                if c.role == 'admin':
                    request.session['role'] = 'admin'
                    return render(request, 'admin.html', {'user': user_login})
                ban = Bans.objects.filter(id_user__login=user_login).first()
                if ban is None:
                    return render(request, 'chat.html', {'user': user_login})
                else:
                    return render(request, 'ban.html', {'login': user_login})
            else:
                return render(request, 'login.html', {'error': 'login incorrect', 'form': LoginForm})