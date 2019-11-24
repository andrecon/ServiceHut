from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Gallery
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse

# Built-in Django CreateView
from django.views.generic import ListView, CreateView 

#Handle the redirect back to our homepage 
from django.urls import reverse_lazy 

from . import forms
from . import models
from .models import Event
from .forms import EventForm 
from .forms import GalleryForm


def index(request):
    context = {
        "variable":"Hello World",
        "title":"Index",
    }
    return render(request, "sections/about.html", context=context)