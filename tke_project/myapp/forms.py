from django import forms
from .models import Event
from .models import Gallery
from .models import Volunteer
from datetime import date
from .models import RUSH

from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'created_date', 'max_volunteers', 'status', 'cover', 'post_author', 'address', 'city', 'state']
    
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['email', 'phone_number', 'event']

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
        fields = ('first_name', 'last_name', "username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class RushTke(forms.ModelForm):
    class Meta:
        model = RUSH
        fields = ['name', 'lastName', 'email','phone_number' ,'year', 'whyTke']
