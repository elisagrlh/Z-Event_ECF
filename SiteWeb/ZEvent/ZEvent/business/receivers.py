from django.db.models.signals import user_logged_in
from django.dispatch import receiver
from .models import UserData

'''
@receiver(user_logged_in)
def increment_login_count(sender, user, **kwargs):
    if user.last_login is not None:  # Pour ignorer la toute première connexion
        profile, created = UserData.objects.get_or_create(user=user)
        profile.login_count += 1
        profile.save()
'''