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
from .forms import EventForm 
from .forms import GalleryForm

import dateutil.parser

def index(request):
    form_instance = forms.EventForm()
    event_query = models.Event.objects.all()
    post_list = {"events":[]}

    for s_q in event_query:
        date_only = s_q.published_date.strftime("%Y-%M-%d")
        post_list["events"] += [{
            "id":s_q.id,
            "title":s_q.title,
            "post_author":s_q.post_author,
            "published_date":date_only,
            "created_date":s_q.created_date,
            "description":s_q.description,
            "max_volunteers":s_q.max_volunteers,
            "cover":s_q.cover,
            "status": s_q.status,
            "current_volunteers": s_q.current_volunteers
            }]
    context = {
        "variable":"Hello World",
        "title":"Index",
        "form":form_instance,
        "some_list":post_list["events"]
    }
    return render(request, "sections/account.html", context=context)

class EventView(ListView):
    model = Event
    template_name = 'sections/account.html'