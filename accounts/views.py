from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserForm, ProfileForm
from .models import Profile

@login_required
def index(request):
    return render(request, 'user-list.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user            
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            raw_user = authenticate(username=username, password=password)
            login(request, raw_user)

            messages.success(request,f'Your account has been created!')
            return redirect('user-list')
    else:
        form = UserForm()
        profile_form = ProfileForm()
    
    context = {'form':form, 'profile_form':profile_form}
    return render(request,'register.html', context)
