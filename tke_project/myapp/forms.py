from django import forms
from .models import Event
from .models import Gallery
from datetime import date
from .models import RUSH

from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    # title = forms.CharField(label='title', max_length=240)
    # description = forms.CharField(label='description', max_length=240)
    # created_date = forms.DateField(label='created Date')
    # max_volunteers = forms.IntegerField(label='max_volunteers')
    # status = forms.BooleanField(label='status', initial=True)
    # cover = forms.ImageField(label="cover")
    
    
    # def save(self, request, commit=True):
    #     new_event = models.Event (
    #         title = self.cleaned_data["title"],
    #         description = self.cleaned_data["description"],
    #         created_date = self.cleaned_data["created_date"],
    #         max_volunteers = self.cleaned_data["max_volunteers"],
    #         cover = self.cleaned_data["cover"],
    #         status = self.cleaned_data["status"],
    #         post_author = request.user
    #     )
    #     print(new_event)
    #     new_event = super().save(commit=False)
    #     if not new_event.pk:
    #         new_event.user = get_user(self.request)
    #     if commit:
    #         new_event.save()
    #         self.save_m2m()
    #     return new_event

    class Meta:
        model = Event
        fields = ['title', 'description', 'created_date', 'max_volunteers', 'status', 'cover', 'post_author']
    
    # def save(self, commit=True):
    #     post = super().save(commit=False)
    #     post.title = self.cleaned_data["title"]
    #     post.description = self.cleaned_data["description"]
    #     post.created_date = self.cleaned_data["created_date"]
    #     post.max_volunteers = self.cleaned_data["max_volunteers"]
    #     post.status = self.cleaned_data["status"]
    #     post.cover = self.cleaned_data["cover"]
    #     post.post_author = User.username
    #     print(post)
    #     if commit:
    #         user.save()
    #     return user


    # def save(self, commit=True):
    #      event = super().save(commit=False)
    #      if not event.pk:
    #         event.user = get_user(self.request)
    #      if commit:
    #          event.save()
    #          self.save_m2m()
    #      return event
    # created_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['title', 'Image']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class RushTke(forms.ModelForm):
    class Meta:
        model = RUSH
        fields = ['name', 'lastName', 'email','phone_number' ,'year', 'whyTke']
