from django.shortcuts import render
from django.views import View
from 
from django.http import HttpResponseRedirect

from .models import UserProfile
from .forms import ProfileForm

# Create your views here.

class CreateProfileView(View):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


# class CreateProfileView(View):

#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         profile = UserProfile(image=request.FILES["user_image"])
#         profile.save()
#         return HttpResponseRedirect("/profiles")


# def store_file(self, request):
#     submitted_form = ProfileForm(request.POST, request.FILES)

#     if submitted_form.is_valid():
#         store_file(request.FILES["image"])
#         return HttpResponseRedirect('/profiles')

#     return render(request, "profiles/create_profile.html",
#                   {"form": submitted_form})
