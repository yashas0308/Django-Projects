from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView
)

# Create your views here.
# def articles_detail_view(request, id):
#     art = Article.objects.get(id=id)
#     context = {
#         'Name' : art.blogauthor,
#         'Title' : art.blogtitle,
#         'BlogDesc' : art.blogcontent,
#         'Date' : art.publishdate,
#         'Category' : art.blogcategory,
#         'name' : "Welcome to Blog",
#     }
#     return render(request, 'blog/article_detail.html', context)

class articles_list_view(ListView):
    
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()


class articles_detail_view(DetailView):
    
    template_name = 'blog/article_detail.html'
    queryset = Article.objects.all()
