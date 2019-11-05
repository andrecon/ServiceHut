from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Gallery
# Create your views here.
from django.http import HttpResponse

# Built-in Django CreateView
from django.views.generic import ListView, CreateView 

#Handle the redirect back to our homepage 
from django.urls import reverse_lazy 

from . import forms
from . import models
from .models import Event
from .forms import EventForm 
from .forms import GalleryForm


# def index(request):
#     context = {
#         "variable":"App",
#         "title":"TKE",
#     }
#     return render(request, "sections/philanthropy.html", context=context)

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
    if request.method == "POST":
        if request.user.is_authenticated:
            form_instance = forms.EventForm(request.POST)
            if form_instance.is_valid():
                new_event = models.Event(title=form_instance.cleaned_data["title"])
                new_event.author = request.user
                new_event.save()
                form_instance = forms.EventForm()
        else:
            form_instance = forms.EventForm()
    else:
        form_instance = forms.EventForm()
    event_query = models.Event.objects.all()
    post_list = {"events":[]}
    for s_q in event_query:
        post_list["events"] += [{
            "id":s_q.id,
            "title":s_q.title,
            "post_author":s_q.post_author.username,
            "created_date":s_q.created_date,
            "description":s_q.description,
            "max_volunteers":s_q.max_volunteers,
            "cover":s_q.cover,
            "status": s_q.status
            }]
    context = {
        "variable":"Hello World",
        "title":"Index",
        "form":form_instance,
        "some_list":post_list["events"]
    }
    return render(request, "sections/philanthropy.html", context=context)