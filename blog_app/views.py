from django.shortcuts import render
from .models import Article
# Create your views here.


def article_details(request,pk):
    articles = Article.objects.get(id=pk)
    return render(request,'blog_app/post-details.html', {"articles":articles})