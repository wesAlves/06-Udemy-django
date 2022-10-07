from django.urls import path
from .views import Index, Posts

urlpatterns = [
    path('', Index.as_view()),
    path('posts/', Posts.as_view()),
    path('posts/<str:slug>', Posts.as_view())
]
