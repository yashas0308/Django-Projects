from django.urls import path, include
from . import views
from .views import ContactsApiView, ContactsDetailView, GenericApiView, ContactViewSet, ContactGenericViewSet, ContactModalViewSet
from rest_framework.routers import DefaultRouter


app_name = 'contacts'

router = DefaultRouter()
# router.register('contact', ContactViewSet, basename='contact')  # Use this for Creating or Defining your own ViewSet for APP.
# router.register('contact', ContactGenericViewSet, basename='contact')  # Use this for Making a Generic ViewSet for APP where methods are prebuilt.
router.register('contact', ContactModalViewSet, basename='contact') # Use this for making more faster, here everything is inbuilt into ModelViewSet.

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('data/', views.contacts, name='contact-data'),
    # path('list/', views.contact_list, name='contact-list'),
    path('list/', ContactsApiView.as_view(), name='contact-list'),
    # path('detail/<int:pk>/', views.contact_detail, name='contact-detail'),
    path('detail/<int:id>/', ContactsDetailView.as_view(), name='contact-detail'),
    path('generic/list/<int:id>/', GenericApiView.as_view(), name='generic-contact-list'),
]
