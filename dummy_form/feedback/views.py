from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'feedback/feedback.html'
    success_url = "/reviews/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankyouView(TemplateView):
    template_name = "feedback/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "this is works"

        return context


class ReviewListView(ListView):
    template_name = "feedback/review_list.html"
    model = Review
    context_object_name = 'reviews'


class ReviewDetailView(DetailView):
    template_name = "feedback/review_detail.html"
    model = Review
