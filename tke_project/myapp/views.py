from django.shortcuts import render
from .models import Gallery
# Create your views here.
from django.http import HttpResponse

# Built-in Django CreateView
from django.views.generic import ListView, CreateView 

#Handle the redirect back to our homepage 
from django.urls import reverse_lazy 

# Create your views here.
from django.http import HttpResponse
from .forms import GalleryForm

from django.contrib.auth.forms import UserCreationForm
from django.views import generic

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

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'