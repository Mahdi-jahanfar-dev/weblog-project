from django.shortcuts import render
from account_app.views import login_user
from blog_app.models import Article
def index(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all().order_by('-pub_date')[:3]
    return render(request, 'main_app/index.html', context={'article': articles})