from _csv import writer

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from .models import Article, Category, Comment, Contactus
from django.core.paginator import Paginator
from .forms import Contactusform
from django.views.generic.base import View, TemplateView, RedirectView

#for all article or something like that django builtin def
from django.views.generic import ListView, DetailView, ArchiveIndexView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import Contactusform, CreatePostForm
from .mixins import LoginRequiredMixin
# Create your views here.


#post detail view
def article_details(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        content = request.POST.get('content')
        parent = request.POST.get('patent_id')
        Comment.objects.create(user=request.user, content=content, parent_id=parent, article=articles)
        return redirect('blog_app:details', slug=slug)
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

# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'blog_app/post-details.html'
#     context_object_name = 'articles'

def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    return render(request, 'blog_app/blog.html', {'articles': page_articles})

def contact_us(request):
    if request.method == 'POST':
        form = Contactusform(data=request.POST)
        if form.is_valid():
            # 1_this way can be use :
            # name = form.cleaned_data['name']
            # content = form.cleaned_data['content']
            # email = form.cleaned_data['email']
            # Contactusl.objects.create(name=name, content=content, emai=email)

            form.save()

            # instance = form.save()
            # and we can do lot of thing with this instance like :
            # instance.name = 'something'
            # or instance.age += 1
            return redirect('blog_app:contactus')
    else:

        form = Contactusform()

    return render(request, 'blog_app/contact.html', {'form': form})

#class based views

#for run the mixin(LoginrequiredMixin) you should use it first in arguments like blow
class ArticleListView(LoginRequiredMixin, ListView):
    queryset = Article.objects.all()
    #paginating
    paginate_by = 4
    #the defult context_object_name is 'object_list' and we can rename this item with button code
    context_object_name = 'articles'
    template_name = 'blog_app/blog.html'

#another way to show something from database in templage
# class ArticleListView(TemplateView):
#     template_name = 'blog_app/blog.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#
#         return context
#


#redirect class with RedirectView
# class RedirectHomePage(RedirectView):
    #a simple way to addresing
    # url = 'https://codeyad.com'

    #addresing width url name and it has reversse on himself
    # pattern_name = 'main_app:index'

    #it while save this addres in user browser and if you delete it it not will deleted in user browser
    # permanent = True

    #if we whant to do something in this class we using this function:
    # def get_redirect_url(self, *args, **kwargs):
    #     #request is in self
    #     print(self.request.user.username)
    #     return super().get_redirect_url(*args, **kwargs)

#post detail with detailview
# class ArticleDetailView(DetailView):
    #we can just get it a model and it will do our work
    # model = Article
    #it will find a template that name is article_detail defultly
    #if our template has another name we use this :
    # template_name = 'blog_app/post-details.html'
    #and for context that will gave the template , context is defultly is object or model name (article)
    #if we whant gave another name context whe use this :
    # context_object_name = 'something'
    #if we whant gave more than one context to our template we use this:
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['title'] = self.object.title
        # return context
        # now we have two context in our template one is object or model name and one is title

    #if the slug has anothe name we use this :
    # slug_field = 'something'
    #if the slug in blog_app url has another name we use this:
    # slug_url_kwarg = 'something'
    # it will also using for pk:
    # pk_url_kwarg = 'somehting'

    # if we whant to filter our objects that we request, we use this :
    # queryset = Article.objects.filter(is_published=True)
    # now our site just show detail of article that is_published is true

#this is form class and for def is up

class FormViewClass(FormView):
    template_name = 'blog_app/contact.html'
    form_class = Contactusform
    #we should use reverse lazy except reverse
    success_url = reverse_lazy('blog_app:contactus')
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)

class MessageView(CreateView):
    model = Contactus
    fields = ('title', 'text')
    success_url = reverse_lazy('blog_app:contactus')
    template_name = 'blog_app/contact.html'

    #this function will use the user email in email field
    def form_valid(self, form):
        #commit = false : it means the object not gana save just we have an instance of it
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        #then we create objects with save method
        instance.save()
        return super().form_valid(form)

    #we are making a queryset of sended message in contactus template with this method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = Contactus.objects.all()
        return context

    #read some document about get_succsess_url def

#this object As the name suggests will show the list of messages
class MessageList(ListView):
    model = Contactus
    template_name = 'blog_app/message_list.html'

#this object will edit the message information
class MessageUpdateView(UpdateView):
    model = Contactus
    fields = ('title', 'text')
    template_name = 'blog_app/message_list_update.html'
    success_url = reverse_lazy('blog_app:message_list')

#this object will delete the selected message
class MessageDeleteView(DeleteView):
    model = Contactus
    success_url = reverse_lazy('blog_app:message_list')

#this object will order the articles sort by date created or updated
class ArchiveIndexView(ArchiveIndexView):
    model = Article
    date_field = "pub_date"


class CreatePostView(CreateView):
    model = Article
    fields = ['title', 'content', 'category', 'image']
    template_name = 'blog_app/Create_Post.html'
    success_url = reverse_lazy('main_app:index')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.writer = self.request.user
        form.files['blog_images'].temporary_file_path()
        instance.save()
        return super().form_valid(form)