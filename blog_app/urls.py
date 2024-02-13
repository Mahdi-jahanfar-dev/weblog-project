from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('post_list', views.all_articles, name='article_list'),
    path('details/<slug:slug>', views.article_details, name='details')
]