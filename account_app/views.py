from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/login')
    else:
        return render(request,'account_app/login.html')