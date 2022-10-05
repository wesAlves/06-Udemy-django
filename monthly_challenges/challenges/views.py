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
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    return HttpResponse(f"<ul>{list_items}</ul>")


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
        return HttpResponse(f"<h1>{challenge_text}</h1>")
    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")
