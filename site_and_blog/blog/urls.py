from django.urls import path
from .views import Index, Posts

urlpatterns = [
    path('', Index.as_view(), name='starting-page'),
    path('posts/', Posts.as_view(), name='post-page'),
    path('posts/<slug:slug>', Posts.as_view(), name='post-detail-page')
]
