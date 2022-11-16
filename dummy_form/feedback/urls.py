from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name='reviews'),
    path("all/", views.ReviewListView.as_view(), name='reviews_list'),
    path("thank-you/", views.ThankyouView.as_view()),
    # path("thank-you/",
    #      views.TemplateView.as_view(template_name='feedback/thank_you.html'))
]
