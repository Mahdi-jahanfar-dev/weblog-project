from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.urls import reverse
def login_user(request):
    if request.user.is_authenticated == True :
        return redirect(reverse('main_app:index'))
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('main_app:index'))
        else:
            return redirect(reverse('account_app:login'))
    else:
        return render(request,'account_app/login.html', {})

def user_account(request):
    if request.user.is_authenticated == True :
        return render(request,'account_app/user_informations.html', {})
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
        user_name = request.POST["user_name"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST['email']
        print(user_name)
        print(password1)
        print(password2)
        print(email)
        if password1 != password2 :
            context['errors'].append("passwords are not same")
            return render(request, 'account_app/register.html', context)
        if User.objects.filter(username=user_name).exists():
            context['errors'].append("this username is taken")
            return render(request, 'account_app/register.html', context)
        elif User.objects.filter(email=email).exists():
            context['errors'].append("this email is exist")
            return render(request, 'account_app/register.html', context)
        else:
            user = User.objects.create_user(username=user_name, password=password1, email=email)
            user.save()
            login(request, user)
            return redirect(reverse('main_app:index'))
    else:
        return render(request, 'account_app/register.html')

def edit_profile(request):
    if User.is_authenticated:
        if request.method == 'POST':
            father_name = request.POST["father_name"]
            melicode = request.POST["meli_code"]
            image = request.POST["image"]

            Profile.objects.create(user_id=1,father_name=father_name, national_code=melicode, image=image)
            return redirect(reverse('account_app:account'))
        else:
            return render(request, 'account_app/edit_profile.html')