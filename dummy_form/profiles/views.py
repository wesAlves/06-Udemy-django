from django.views import View
from .models import UserProfile
from django.views.generic import ListView

# Create your views here.


class CreateProfileView(View):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"
