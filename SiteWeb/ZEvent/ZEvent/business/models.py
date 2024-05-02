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

# Create your models here


class UserData(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   age = models.PositiveIntegerField()
   def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

def validate_future_date(value):
    if value <= timezone.now():
        raise ValidationError('La date doit être dans le futur.')
    
    
class OptionsMaterial(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
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
    streamer_name = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    theme = models.ManyToManyField(OptionsTheme)
    start_date = models.DateTimeField(validators=[validate_future_date])
    end_date = models.DateTimeField(validators=[validate_future_date])
    pegi = models.IntegerField(choices=PEGI_CHOICES, null=True, blank=True)
    material = models.ManyToManyField(OptionsMaterial)
    def __str__(self):
        # Si streamer_name est None (pas d'utilisateur lié), afficher un texte par défaut
        if self.streamer_name:
            return f"{User.first_name} {User.last_name}"
        else:
            return "No streamer assigned"
