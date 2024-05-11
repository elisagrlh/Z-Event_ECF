from .models import Live, LiveRegistration, LiveStats
from django.shortcuts import get_object_or_404

def get_lives():
    return Live.objects.all()

def get_specific_live(live_id):
    live = get_object_or_404(Live, id=live_id)
    return live

def get_registration_lives():
    return LiveRegistration.objects.all()

def increment_click_stats(live_id):
    live = Live.objects.get(id=live_id)
    stats, created = LiveStats.objects.get_or_create(
        live_id = live_id,
        label=live.label,
        streamer_pseudo=live.streamer_pseudo,
        start_date = live.start_date,
        defaults={'click_nb': 1}
    )
    if not created:
        stats.click_nb += 1
        stats.save(update_fields=['click_nb'])

def get_live_stats():
    return LiveStats.objects.all()
