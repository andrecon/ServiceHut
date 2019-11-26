from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

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
    # post_author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    post_author = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    def __str__(self):
        return self.title

class Volunteer(models.Model):
    email = models.CharField(max_length=100)
    phone_number = PhoneNumberField(default='+1')

    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email', 'phone_number', 'event']



class Gallery(models.Model):
    title = models.TextField()
    Image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title

class RUSH(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = PhoneNumberField(default='+1')
    year = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    whyTke = models.TextField()

    def __str__(self):
        return self.name
