from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView

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


def thank_you(request):
    return render(request, "feedback/thank_you.html")


class ThankyouView(TemplateView):

    template_name = "feedback/thank_you.html"