from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name='reviews'),
    path("all/", views.ReviewView.as_view(), name='reviews_list'),
    path("thank-you/", views.thank_you)
]
