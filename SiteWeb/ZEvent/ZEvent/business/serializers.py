from rest_framework import serializers
from .models import Live

class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live
        fields = ["label", "streamer_name", "theme", "start_date", "end_date", "pegi", "material"]
