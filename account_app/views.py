from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.urls import reverse
from .forms import LoginForm, RegisterForm, Edit_profile_form
from django.core.exceptions import ValidationError
def login_user(request):
    if request.user.is_authenticated == True :
        return redirect(reverse('main_app:index'))
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect(reverse('main_app:index'))
    else:
        form = LoginForm()
    return render(request,'account_app/login.html', {'form': form})

def user_account(request):
    if request.user.is_authenticated == True :
        return render(request,'account_app/profile-info.html', {})
    else:
        return redirect(reverse('main_app:index'))

def user_logout(request):
    if request.user.is_authenticated == True :
        logout(request)
        return redirect(reverse('main_app:index'))

def register(request):
    context = {"errors":[]}
    if request.user.is_authenticated == True :
        return redirect(reverse('main_app:index'))
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'), email=form.cleaned_data.get('email'))
            login(request, user)

            return redirect(reverse('main_app:index'))
        else:
            return render(request,'account_app/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'account_app/register.html', {'form': form})

def edit_profile(request):
    if User.is_authenticated:
        user = request.user
        form = Edit_profile_form(instance=user)
        if request.method == 'POST':
            form = Edit_profile_form(instance=user, data=request.POST)
            if form.is_valid():
                form.save()

        return render(request, 'blog_app/contact.html', {'form': form})
