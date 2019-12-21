from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from .models import Profile

@login_required
def index(request):
    return render(request, 'user-list.html')

@login_required
def newUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user            
            profile.save()

            messages.success(request,f'Usuário criado com sucesso!')
            return redirect('user-list')
    else:
        form = UserForm()
        profile_form = ProfileForm()
    
    context = {'form':form, 'profile_form':profile_form}
    return render(request,'new.html', context)


@login_required
def listUser(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    
    if search:
        users = User.objects.filter(username__icontains=search, username=request.user)
    elif filter:
        users = User.objects.filter(done=filter, username=request.user)

    else:
        users_list = User.objects.all().order_by('-date_joined')#.filter(username=request.user)

        paginator = Paginator(users_list, 3)

        page = request.GET.get('page')
        users = paginator.get_page(page)
    

    return render(request, 'user-list.html', 
        {'users':users})


@login_required
def deleteUser(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()

    messages.info(request, 'Usuário deletado')

    return redirect('user-list')


@login_required
def editUser(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)

    if(request.method == 'POST'):
        form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=user.profile)

        if(form.is_valid()):
            user.save()
            return redirect('user-list')
        else:
            return render(request, 'update.html', {'form': form, 'profile_form':profile_form, 'user': user})
    else:
        return render(request, 'update.html', {'form': form, 'profile_form':profile_form, 'user': user})

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

            messages.success(request,f'Seu usuário foi criado!')
            return redirect('user-list')
    else:
        form = UserForm()
        profile_form = ProfileForm()
    
    context = {'form':form, 'profile_form':profile_form}
    return render(request,'register.html', context)
