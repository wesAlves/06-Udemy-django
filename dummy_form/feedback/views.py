from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm  #we don't need this field but we could use that to pass extra configurations to our view
    template_name = 'feedback/feedback.html'
    success_url = "/reviews/thank-you"


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session["favorite_review"]
        context['is_favorite'] = favorite_id == str(loaded_review.id)

        return context


class AddFavoriteView(View):

    def post(self, request):
        review_id = request.POST['review_id']
        # fav_review = Review.objects.get(pk=review_id) #It is smarttest to store just simple data into data bases, so we decided to store just the review id

        request.session["favorite_review"] = review_id

        return HttpResponseRedirect("")
