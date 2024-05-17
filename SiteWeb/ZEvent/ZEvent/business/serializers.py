from rest_framework import serializers
from .models import Live, LiveStats
from .models import UserData
from .models import OptionsTheme
from .models import OptionsMaterial
from django.contrib.auth.models import User
import logging


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['pseudo']

class OptionsMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsMaterial
        fields = ['label', 'brand']


class OptionsThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsTheme
        fields = ['name']

class LiveSerializer(serializers.ModelSerializer):
    #streamer_first_name = serializers.CharField(source='streamer_name.first_name', read_only=True)
    #streamer_last_name = serializers.CharField(source='streamer_name.last_name', read_only=True)
    # retrieve foreignkeys to later change them in char and not id
    streamer_pseudo = serializers.CharField(source='streamer_pseudo.pseudo', read_only=True)
    material= OptionsMaterialSerializer(many=True)
    theme = OptionsThemeSerializer(many=True)

    class Meta:
        model = Live
        fields = ['id', 'label', 'streamer_pseudo', 'theme', 'start_date', 'end_date', 'pegi', 'material']

class LiveStatsSerializer(serializers.ModelSerializer):
    #start_date = LiveSerializer(source="start_date.start_date")
    #start_date = serializers.DateTimeField(source='live.start_date', read_only=True)

    class Meta:
        model = LiveStats
        fields = ['live_id', 'click_nb', 'label', 'streamer_pseudo', 'start_date']


class StreamerLivesSerializer(serializers.ModelSerializer):
    lives = LiveSerializer(many=True, read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)



    class Meta:
        model = UserData
        fields = ['pseudo', 'email', 'first_name', 'last_name', 'lives']        

