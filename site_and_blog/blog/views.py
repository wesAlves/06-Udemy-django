from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# TODO: / load starting page with list latests block post and some welcome text
# TODO: /post  load page with list all blog posts
# TODO: /post/<slug> load individual blog post page with shows full  blog post

class Index (View):
    
    def get(self, request):
        return render(request, "blog/index.html")


class Posts (View):

    def get(self, request):
        return render(request, "blog/all-post.html")


class PostsDetails (View):
    pass

    # def get(self, request, slug):
    #     return HttpResponse('index')