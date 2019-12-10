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

# A page representing a list of objects.
class EventView(ListView):
    model = Event
    template_name = 'sections/philanthropy.html'

class CreateEventView(CreateView): 
    model = Event
    form_class = EventForm
    template_name = 'sections/post.html'
    success_url = reverse_lazy('philanthropy')


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
            "current_volunteers": s_q.current_volunteers,
            "address": s_q.address,
            "city": s_q.city,
            "state": s_q.state
            }]
    context = {
        "variable":"Hello World",
        "title":"Index",
        "form":form_instance,
        "some_list":post_list["events"]
    }
    return render(request, "sections/philanthropy.html", context=context)


@csrf_exempt
@login_required(login_url='/login/')
def posts_view(request):
    if request.method == "GET":
        event_query = models.Event.objects.all().order_by('-created_date')
        post_list = {"events":[]}

        suggestion_list = {"events":[]}
        for s_q in event_query:
            url = ""
            if not str(s_q.cover)=="":
                url=s_q.cover.url
            date_only = s_q.published_date.strftime("%Y-%M-%d")
            post_list["events"] += [{
                "title":s_q.title,
                "post_author":s_q.post_author,
                "created_date":s_q.created_date,
                "description":s_q.description,
                "max_volunteers":s_q.max_volunteers,
                "cover":url,
                "status":s_q.status,
                "published_date":date_only,
                "current_volunteers": s_q.current_volunteers
                }]
        return JsonResponse(post_list)
    return HttpResponse("Unsupported HTTP Method")