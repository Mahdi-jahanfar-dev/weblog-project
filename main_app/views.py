from django.shortcuts import render
from account_app.views import login_user
from blog_app.models import Article
def index(request):
    articles = Article.objects.all()
    return render(request, 'main_app/index.html', context={'article': articles})