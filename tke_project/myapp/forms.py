from django import forms
from .models import Event
from .models import Gallery
from datetime import date

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):

    # created_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    
    class Meta:
        model = Event
        fields = ['title', 'description', 'created_date', 'max_volunteers', 'status', 'cover']

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
