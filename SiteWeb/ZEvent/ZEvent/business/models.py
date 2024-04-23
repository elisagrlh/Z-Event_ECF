import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here


class UserData(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   age = models.PositiveIntegerField()
   def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    

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
    streamer_name = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    theme = models.ManyToManyField(OptionsTheme)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    pegi = models.IntegerField(choices=PEGI_CHOICES, null=True, blank=True)
    material = models.ManyToManyField(OptionsMaterial)
    def __str__(self):
        # Si streamer_name est None (pas d'utilisateur lié), afficher un texte par défaut
        if self.streamer_name:
            return f"{User.first_name} {User.last_name}"
        else:
            return "No streamer assigned"
