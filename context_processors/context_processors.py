from blog_app.models import Article, Category


def recent_posts(request):
    posts = Article.objects.order_by('-pub_date')[:3]
    return {'recent_art': posts}

def categories_list(request):
    categories = Category.objects.all()
    return {'categories': categories}