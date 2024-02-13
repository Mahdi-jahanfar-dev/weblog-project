from blog_app.models import Article


def recent_posts(request):
    posts = Article.objects.order_by('-pub_date')[:3]
    return {'recent_art':posts}