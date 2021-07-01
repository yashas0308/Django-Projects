from django.urls import path, include
from .views import StudentViews
from rest_framework.routers import DefaultRouter

app_name = 'school'

router = DefaultRouter()
router.register('', StudentViews, basename='student')

urlpatterns = [
    path('api/', include(router.urls)),
]