from django.db import models
from datetime import datetime

# Create your models here.


class Event(models.Model):
    title = models.TextField()
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True, blank=True) #Current date
    created_date = models.DateField()  #Future Date
    max_volunteers = models.IntegerField(default=1)
    current_volunteers = models.IntegerField(default=1)
    cover = models.ImageField(upload_to='event_images/')

    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.TextField()
    Image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title
