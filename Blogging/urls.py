from django.urls import path
from .views import BloglistAPIView

urlpatterns = [
    path('blogs/', BloglistAPIView.as_view(), name= 'Blog-list'),
]
