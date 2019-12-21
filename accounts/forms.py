from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1']

        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Usuário',
            'password1': 'Senha'
        }


    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth']

        widgets = {
            'birth': forms.DateInput(),
        }
        labels = {
            'birth' : 'Data de nascimento'
        }

        help_texts = {
            'birth': 'Formato: YYYY-MM-DD'
        }
