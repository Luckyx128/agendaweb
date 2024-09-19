# minha_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class FormularioDeRegistro(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class FormularioDeLogin(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
