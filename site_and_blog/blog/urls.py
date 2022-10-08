from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='starting-page'),
    path('posts/', views.Posts, name='post-page'),
    path('posts/<slug:slug>', views.Posts_details, name='post-detail-page')
]
