from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models

User = get_user_model()  # Dynamically gets your active custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Specify the fields you want to show in the signup form.
        # For example, if you added 'first_name' or custom fields:
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'rut')

class ActualizarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

        labels = {
            "username": "Nombre de usuario",
            "email": "Email",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }

class NuevoInmuebleForm(forms.ModelForm):
    class Meta:
        model = models.Inmueble
        exclude = ["dueno"]

class ActualizarInmuebleForm(forms.ModelForm):
    class Meta:
        model = models.Inmueble
        exclude = ["dueno"]
