from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# TODO: / load starting page with list latests block post and some welcome text
# TODO: /post  load page with list all blog posts
# TODO: /post/<slug> load individual blog post page with shows full  blog post

def Index (request):
    return render(request, "blog/index.html")


def Posts (request):
    return render(request, "blog/all-post.html")


def Posts_details (request, slug):
    return render(request, "blog/post-detail.html" )