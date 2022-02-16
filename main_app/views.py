from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import City, Post, Profile, User
from django.contrib.auth.models import User
from  django import forms
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name  = forms.CharField()

    class Meta:
	    model = User
	    fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class Signup(View):
    def get(self, request):
        form = RegisterForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/create-profile/")
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

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'img', 'city']
    template_name = 'post_create.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'img', 'city']
    template_name = "post_update.html"
    success_url = '/posts/'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
    success_url = '/posts/'

class ProfileCreate(CreateView):
    model = Profile
    fields = ['img', 'current_city', 'bio']
    template_name = 'create_profile.html'
    
    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})
    # success_url = f"/nomads/{current_user}"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

    # def get_context_data(self, **kwargs):
    #     context = super(CreateView, self).get_context_data(**kwargs)
    #     context['user'] = User.objects.get(id = self.request.user.id)
    #     return context

# create_user(username, email=None, password=None, **extra_fields)
