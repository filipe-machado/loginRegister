from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method=="POST":
        user_form = UserForm(request.POST)
        profile_form=ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save
            user_form.save()
            username=user_form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created!')
            return redirect('login')
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
    
    return render(request,'register.html',{'user_form':user_form, 'profile_form':profile_form})



""" from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import UserForm, ProfileForm
# Create your views here.

class SignUpView(View):
    templateName = 'register.html'

    def get(self, request, *arg, **kwargs):
        form = UserCreationForm()
        profile_form = ProfileForm()
        return render(request, self.templateName, {'form': form})

    def post(self, request, *arg, **kwargs):
        form = UserCreationForm(request.POST, request.user)
        profile_form = ProfileForm(request.POST, request.user)
        if form.is_valid():
            user = form.save()
            profile_user = profile_form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        return render(request, self.templateName, {'form': form, 'profile_form': profile_form}) """


""" 
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm


def register(request):
    user_form = UserForm(request.POST or None)
    profile_form=ProfileForm()

    context = {'user_form':user_form, 'profile_form':profile_form}
    if request.method == 'POST':
        if user_form.is_valid() and profile_form():
            user_form.save()
            profile_form.save()
    return render(request, 'register.html', context)
 """