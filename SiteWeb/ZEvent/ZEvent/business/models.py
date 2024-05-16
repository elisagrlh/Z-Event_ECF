import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
#from django.db.models.signals import user_logged_in
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils import timezone
from djongo import models

# Create your models here


class UserData(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   age = models.PositiveIntegerField()
   pseudo = models.CharField(max_length=50)
   def __str__(self):
        return self.pseudo
    

def validate_future_date(value):
    if value <= timezone.now():
        raise ValidationError('La date doit être dans le futur.')
    
    
class OptionsMaterial(models.Model):
    label = models.CharField(max_length=300)
    brand = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.label} ({self.brand})"



class OptionsTheme(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name


class Live(models.Model):
    PEGI_CHOICES = [
        (12, '12'),
        (16, '16'),
        (18, '18'),
    ]
    label = models.CharField(max_length=50)
    streamer_pseudo = models.ForeignKey(UserData, null=False, blank=False, on_delete=models.CASCADE)
    theme = models.ManyToManyField(OptionsTheme)
    start_date = models.DateTimeField(validators=[validate_future_date])
    end_date = models.DateTimeField(validators=[validate_future_date])
    pegi = models.IntegerField(choices=PEGI_CHOICES, null=True, blank=True)
    material = models.ManyToManyField(OptionsMaterial, blank=True)


class LiveRegistration(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    live = models.ForeignKey(Live, on_delete=models.CASCADE)

class LiveStats(models.Model):
    live_id = models.PositiveIntegerField(primary_key=True)
    click_nb = models.PositiveIntegerField()
    label = models.CharField(max_length=50)
    streamer_pseudo = models.CharField(max_length=50)
    start_date = models.DateTimeField()