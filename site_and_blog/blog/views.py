from datetime import date
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

all_posts = [
    {
    "slug" : "hike-in-the-mountains",
    "image" : 'mountains.jpg',
    "author": "Max",
    "date" : date(2022, 10, 8),
    "title": "Hiking mountains",
    "excerpt": 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consectetur saepe repudiandae officiis delectus illum. Dignissimos vel praesentium, voluptas officia laborum minus fugiat dolore iure recusandae iste, in maxime, molestias natus.',
    "content": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consectetur saepe repudiandae officiis delectus illum. Dignissimos vel praesentium, voluptas officia laborum minus fugiat dolore iure recusandae iste, in maxime, molestias natus."
},{
    "slug" : "hike-in-the-mountains-2",
    "image" : 'mountains.jpg',
    "author": "Max",
    "date" : date(2022, 10, 8),
    "title": "Hiking mountains 2",
    "excerpt": 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consectetur saepe repudiandae officiis delectus illum. Dignissimos vel praesentium, voluptas officia laborum minus fugiat dolore iure recusandae iste, in maxime, molestias natus.',
    "content": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consectetur saepe repudiandae officiis delectus illum. Dignissimos vel praesentium, voluptas officia laborum minus fugiat dolore iure recusandae iste, in maxime, molestias natus."
}
]

# Create your views here.

#helper temporaryly
def get_date(post):
    return post['date']

def Index (request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_post = sorted_post[-3:]

    return render(request, "blog/index.html", context={ "posts" : latest_post })


def Posts (request):
    return render(request, "blog/all-post.html")


def Posts_details (request, slug):
    return render(request, "blog/post-detail.html" )