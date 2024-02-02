from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user),
    path('account',views.user_account),
    path('logout',views.user_logout),
    path('register',views.register)
]