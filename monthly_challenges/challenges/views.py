from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

monthly_challenges = {
    'jan': 'January content',
    'feb': 'Feb content',
    'mar': 'mar content',
    'apr': 'apr content',
    'may': 'may content',
    'jun': 'jun content',
    'jul': 'jul content',
    'aug': 'aug content',
    'sep': 'sep content',
    'oct': 'oct content',
    'nov': 'nov content',
    'dez': 'dez content',
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    # build a path that is like this: /challenge + the args
    redirect_path = reverse('month-challenge', args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        # best practice to repeat the app's name in the templates name folder to make django not merge the templates with the same name
        return render(request, 'challenges/challenge.html', {'month_name': month, 'month_challenge': challenge_text})

    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")
