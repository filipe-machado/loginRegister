from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateField()

    def __str__(self):
        return self.user.username
    
