from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
post_save.connect(create_user_profile, sender=User, dispatch_uid="app_models_create_user_profile") 

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

post_save.connect(create_user_profile, sender=User, dispatch_uid="app_models_create_user_profile") 
