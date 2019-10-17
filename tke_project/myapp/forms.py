from django import forms
from .models import Event
from .models import Gallery
from datetime import date

class EventForm(forms.ModelForm):

    # created_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    
    class Meta:
        model = Event
        fields = ['title', 'description', 'created_date', 'max_volunteers', 'status', 'cover']

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['title', 'Image']
