from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse(f"this is working")


def monthly_challenges(request, month):
    return HttpResponse(month)
