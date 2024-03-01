from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment
from django.core.paginator import Paginator
from .forms import Contactform

# Create your views here.


#post detail view
def article_details(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        content = request.POST.get('content')
        parent = request.POST.get('patent_id')
        Comment.objects.create(user=request.user, content=content, parent_id=parent, article=articles)
    recent_articles = Article.objects.all().order_by('-pub_date')[:3]
    return render(request,'blog_app/post-details.html', {"articles": articles})

#all posts view
def all_articles(request):
    articles = Article.objects.all()
    paginatore = Paginator(articles, 4)
    page = request.GET.get('page')
    page_articles = paginatore.get_page(page)
    return render(request, 'blog_app/blog.html', {'articles': page_articles})


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.article.all()
    return render(request, 'blog_app/blog.html', {'articles': articles})

def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    return render(request, 'blog_app/blog.html', {'articles': page_articles})

def contact_us(request):
    form = Contactform()
    return render(request, 'blog_app/contact.html', {'form': form})