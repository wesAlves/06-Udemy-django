from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(View):

    def get(self, request):
        form = ReviewForm()

        return render(request, 'feedback/feedback.html', {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/reviews/thank-you")


class ThankyouView(TemplateView):
    template_name = "feedback/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "this is works"

        return context


class ReviewListView(ListView):
    template_name = "feedback/review_list.html"
    model = Review
    context_object_name = 'reivews'


class ReviewDetailView(TemplateView):
    template_name = "feedback/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.get(pk=kwargs['id'])

        context['review'] = review

        return context