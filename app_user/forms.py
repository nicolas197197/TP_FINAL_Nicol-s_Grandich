from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_user.models import Avatar


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='username', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )        