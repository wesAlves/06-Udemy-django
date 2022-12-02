from datetime import date
from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import Post


def Index(request):
    latest_post = Post.objects.all().order_by("-created_date")[:3]

    return render(request, "blog/index.html", context={"posts": latest_post})


def Posts(request):
    all_posts = Post.objects.all()
    return render(request,
                  "blog/all-post.html",
                  context={'all_posts': all_posts})


def Posts_details(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,
                  "blog/post-detail.html",
                  context={"post": "identified_post"})
