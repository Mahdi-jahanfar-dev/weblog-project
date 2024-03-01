from django.urls import path
from . import views
app_name = 'account_app'
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('account',views.user_account, name='account'),
    path('logout',views.user_logout, name='logout'),
    path('register',views.register, name='register'),
    path('edit_profile',views.edit_profile, name='edit_profile'),
]