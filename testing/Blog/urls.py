from django.urls import path
from .views import articles_detail_view, articles_list_view

app_name = 'Blog'

urlpatterns = [
    path('articlelist/', articles_list_view.as_view(), name='article-list'),
    path('<int:pk>/', articles_detail_view.as_view(), name='article-detail'),
]
