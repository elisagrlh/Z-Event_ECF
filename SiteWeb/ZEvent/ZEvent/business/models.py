import datetime

from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from django.conf import settings
# Create your models here


#class UserData(User):
class UserData(models.Model):
   #user = models.OneToOneField(User, on_delete=models.CASCADE)
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   age = models.PositiveIntegerField()
   username = models.CharField(max_length=140)
   email = models.CharField(max_length=140)
   first_name= models.CharField(max_length=140)
   last_name= models.CharField(max_length=140)




'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #confirmed = models.BooleanField("Confirmed", default=False)

    age = models.IntegerField("age")
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

'''


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
    
