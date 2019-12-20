from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuário'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        }

        help_texts = {
            'username': ''
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth']

        widgets = {
            'birth': forms.DateInput(attrs={'placeholder': 'Data de nascimento'}),
        }
        labels = {
            'birth' : 'Data de nascimento'
        }

        help_texts = {
            'birth': 'YYYY/MM/DD'
        }