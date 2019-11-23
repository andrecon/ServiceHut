from django.contrib import admin

# Register your models here.
from .models import Event
from .models import Gallery
from .models import RUSH
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(RUSH)