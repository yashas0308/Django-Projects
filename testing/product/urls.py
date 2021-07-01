from django.urls import path, include
from . import views
from .views import ProductModelViewSets, UserList, UserDetail
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

app_name = "product"

router = DefaultRouter()
router.register('product', ProductModelViewSets, basename='product')

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register/', views.registration_view, name='register'),
    path('login/', obtain_auth_token,  name='login'),
    path('viewset/', include(router.urls)), 
    path('viewset/<int:pk>/', include(router.urls)),
    path('product/', views.product_view_detail, name='product'), 
    path('product/list/', views.product_list_view, name='product-list'),
    path('product/<int:my_id>/', views.dynamic_loookup_url, name='product-url'),
    path('product/<int:id>/delete/', views.product_delete_view, name='product-delete'),
    path('create', views.product_create_detail, name='product-create'), 
]

# path('register/', views.register_user, name='register'),