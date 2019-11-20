from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Gallery
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import json
# Create your views here.
from django.http import HttpResponse

# Built-in Django CreateView
from django.views.generic import ListView, CreateView 

#Handle the redirect back to our homepage 
from django.urls import reverse_lazy 

# Create your views here.
from django.http import HttpResponse
from . import forms
from . import models
from .forms import GalleryForm

# from django.contrib.auth.forms import UserCreationForm
# from django.views import generic

def index(request):
    context = {
        "variable":"App",
        "title":"TKE",
    }
    return render(request, "index.html", context=context)

# A page representing a list of objects.
class GalleryView(ListView):
    model = Gallery
    template_name = 'index.html'

class CreateImageView(CreateView): 
    model = Gallery
    form_class = GalleryForm
    template_name = 'sections/PhotoPost.html'
    success_url = reverse_lazy('index')

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def signup(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
            # print("Hi")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/signup.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")

def contact(request):
    return render(request, "sections/contact.html")

def chat(request):
    
    return render(request,"sections/chat.html", {})

def room(request, room_name):
    return render(request,'sections/room.html',{
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })