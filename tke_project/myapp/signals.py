from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models

@receiver(post_save,sender=Volunteer)
def on_batch_child_saving(sender,instance,**kwargs):
    event_instance = Event.objects.get(pk=instance.event)
    print(event_instance)

    # if (event_instance.current_volunteers < event_instance.max_volunteers): 
    event_instance.current_volunteers = 10
    event_instance.save()

    # else:
    #     print("error")