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

def get_display_value(value):
    if hasattr(value, 'all'):
        # For QuerySet, we need to list the names
        return ', '.join([str(item) for item in value.all()])
    if isinstance(value, list):
        return ', '.join([str(item) for item in value])
    return str(value)

def format_changes(changes):
    formatted_changes = []
    for field, (old_value, new_value) in changes.items():
        old_value_str = get_display_value(old_value) if old_value is not None else 'None'
        new_value_str = get_display_value(new_value) if new_value is not None else 'None'
        formatted_changes.append(f"{field}: {new_value_str}")
    return "\n".join(formatted_changes)