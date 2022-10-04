from django.http import HttpResponse, HttpResponseNotFound
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


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not supported")
