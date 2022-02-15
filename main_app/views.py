from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import City, Post, Profile, User
from django.contrib.auth.models import User

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

class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.filter(id = self.kwargs['pk'])
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

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'img', 'city', 'author']
    template_name = 'post_create.html'
    success_url = '/posts/'

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'img', 'city']
    template_name = "post_update.html"
    success_url = '/posts/'

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
    success_url = '/posts/'