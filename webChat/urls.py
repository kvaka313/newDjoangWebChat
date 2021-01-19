"""webChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from MyWebChat.bun import get_all_users, add_user_to_bl, del_user_from_bl
from MyWebChat.views import RegistrationView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('registration_handler', RegistrationView.as_view(), name='registration_handler'),
    path('login/', LoginView.as_view(), name='login'),
    path('login_handler', LoginView.as_view(), name='login'),
    path('get_users/', get_all_users),
    path('add_user', add_user_to_bl),
    path('delete_user/<str:name>/', del_user_from_bl),
]