from .models import Live
from django.shortcuts import get_object_or_404

def get_lives():
    return Live.objects.all()

def get_specific_live(live_id):
    live = get_object_or_404(Live, id=live_id)
    return live