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
    return HttpResponse(f"this is working")


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
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not supported")
