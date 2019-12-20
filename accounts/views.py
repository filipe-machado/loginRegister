from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method=="POST":
        user_form=UserForm(request.POST)
        profile_form=ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()             
            profile_form.save()             
            username=user_form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created!')
            return redirect('login')
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
    
    return render(request,'register.html',{'user_form':user_form, 'profile_form':profile_form})