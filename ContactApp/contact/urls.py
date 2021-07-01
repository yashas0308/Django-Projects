from django.urls import path, include
from . import views
from .views import ContactList, PhoneNumList
from rest_framework.routers import DefaultRouter

app_name = 'contact'

router2 = router = DefaultRouter()
router.register(r'contact_ls', ContactList, basename='contactlist')
router2.register(r'phone_ls', PhoneNumList, basename='phonelist')

urlpatterns = [
    path(r'^', include(router.urls)),
    path(r'^', include(router2.urls)),
    path('', views.contact_list, name='contact_list'),
    path('person/<int:pk>', views.contact_detail, name='contact_detail'),
    path('person/new', views.contact_new, name='contact_new'),
    path('person/<int:pk>/edit', views.contact_edit, name='contact_edit'),
    path('person/<int:pk>/delete', views.contact_delete, name='contact_delete'),
]
