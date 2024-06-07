from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    #old function base view
    # path('post_list', views.all_articles, name='article_list'),

    #we can also fill the class variables in 'as_view' like this :
    # path('post_list', views.ArticleListView.as_view(model = something), name='article_list'),
    path('post_list', views.ArticleListView.as_view(), name='article_list'),
    path('details/<slug:slug>', views.article_details, name='details'),
    path('cat_details/<slug:slug>', views.category_details, name='category_details'),
    path('search/', views.search, name='search'),
    # path('contact/', views.contact_us, name='contactus')
    path('contact/', views.MessageView.as_view(), name='contactus'),
    path('messages', views.MessageList.as_view(), name='message_list'),
    path('message/edit/<int:pk>', views.MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>', views.MessageDeleteView.as_view(), name='message_delete'),
    path('archive', views.ArchiveIndexView.as_view(), name='article_archive'),
    path('createpost', views.CreatePostView.as_view(), name='createpost')
]