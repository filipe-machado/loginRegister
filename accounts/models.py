from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Profile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
