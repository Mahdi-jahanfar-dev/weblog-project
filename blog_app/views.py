from django.shortcuts import render , get_object_or_404, redirect
from .models import Article
# Create your views here.


def article_details(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    recent_articles = Article.objects.all().order_by('-pub_date')[:3]
    return render(request,'blog_app/post-details.html', {"articles": articles, 'recent_articles': recent_articles})


def all_articles(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all().order_by('-pub_date')[:3]
    return render(request, 'blog_app/blog.html', {'articles': articles, 'recent_articles': recent_articles})