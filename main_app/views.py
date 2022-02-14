from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import City, Post, Profile, Comment
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context ={"form": form}
            return render(request, "registration/signup.html", context)

class CityList(TemplateView):
    template_name = "city_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        return context

class CityDetail(DetailView):
    model = City
    template_name = "city_detail.html"

class ProfileList(TemplateView):
    template_name = "profile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context

class ProfileDetail(TemplateView):
    template_name = "profile_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk = pk)
        return context

class PostList(TemplateView):
    template_name = "post_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()        
        return context
    
class PostDetail(DetailView):
        model = Post
        template_name = "post_detail.html"
