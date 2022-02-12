from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


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