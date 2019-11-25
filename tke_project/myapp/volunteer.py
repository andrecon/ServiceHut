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
from django.contrib.auth.models import User

from . import forms
from . import models
from .models import Event
from .models import Volunteer
from .forms import EventForm 
from .forms import GalleryForm

import dateutil.parser


class CreateVolunteerView(CreateView): 
    model = Volunteer
    form_class = EventForm
    template_name = 'sectiontions/volunteer.html'
    success_url = reverse_lazy('philanthropy')