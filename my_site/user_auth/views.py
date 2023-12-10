from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def user_register(request):
    if request.method == "POST":
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('name:index')
    register_form = NewUserForm
    return render(request=request, template_name='user_auth/register.html', context={'register_form': register_form})

def user_login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('name:index')
    
    login_form = AuthenticationForm()
    return render(request=request, template_name='user_auth/login.html', context={'login_form': login_form})