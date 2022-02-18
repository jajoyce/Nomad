from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import City, Post, Profile, User, Comment
from django.contrib.auth.models import User
from  django import forms


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(id__lte=3)
        return context

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
            return redirect("/nomads/new")
        else:
            context ={"form": form}
            return render(request, "registration/signup.html", context)

class UserUpdate(UpdateView):
    model = User
    fields = ["username", "email", "first_name", "last_name"]
    template_name ='registration/user_update.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.profile.pk})

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
        context['profileuser'] = User.objects.filter(id = self.kwargs['pk'])
        return context

class PostList(TemplateView):
    template_name = "post_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()        
        return context
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        post = Post.objects.filter(id=self.kwargs['pk'])[0]

        if form.is_valid():
            user = request.user
            content = form.cleaned_data['content']
            comment = Comment.objects.create(author_id=user.id, post=post, content=content)
            context['form'] = CommentForm()
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'img', 'city']
    template_name = 'post_create.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostCityCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'img']
    template_name = 'post_create.html'
    success_url = '/posts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_preselected'] = True
        context['city_name'] = City.objects.filter(id=self.kwargs['pk'])[0]
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.city = City.objects.filter(id=self.kwargs['pk'])[0]
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
    template_name = 'profile_create.html'
    
    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Loggedin(View):
    def get(self, request):
        user = request.user
        return redirect(f'/nomads/{user.profile.pk}')

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['content']
    template_name = "comment_update.html"
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})
    
class CommentDelete(DeleteView):
    model = Comment
    template_name = "comment_delete_confirmation.html"
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['current_city', 'bio', 'img']
    template_name = 'profile_update.html'

    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})

class ProfileDelete(DeleteView):
    model = Profile
    template_name = "profile_delete_confirmation.html"
    success_url = "/"

