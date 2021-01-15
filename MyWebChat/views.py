from django.shortcuts import render
from django.template.backends import django
from django.views.generic import FormView

from MyWebChat.forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return render(request, 'index.html', {})
        return render(request, 'registration.html', {'error': 'error in registration', 'form': RegistrationForm})
