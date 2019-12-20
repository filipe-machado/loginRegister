from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

class ProfileForm(forms.ModelForm):
    birth = forms.DateField()
    class Meta:
        model = Profile
        fields = ['birth']
