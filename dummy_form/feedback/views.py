from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def reviews(request):

    if request.method == 'POST':
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect("/reviews/thank-you")

    return render(request, 'feedback/feedback.html')


def thank_you(request):
    return render(request, "feedback/thank_you.html")