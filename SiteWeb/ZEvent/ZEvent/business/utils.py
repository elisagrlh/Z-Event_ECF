from .models import Live, LiveRegistration
from django.shortcuts import get_object_or_404

def get_lives():
    return Live.objects.all()

def get_specific_live(live_id):
    live = get_object_or_404(Live, id=live_id)
    return live

def get_registration_lives():
    return LiveRegistration.objects.all()