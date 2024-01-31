from django.shortcuts import render
from account_app.views import login_user
def index(request):
    return render(request,'main_app/index.html' , context={'user':login_user})