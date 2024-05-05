from rest_framework import serializers
from .models import Live
from .models import UserData
from .models import OptionsMaterial
from .models import OptionsTheme
from django.contrib.auth.models import User


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
    material_label = OptionsMaterialSerializer(source='material', many=True)
    material_brand = OptionsMaterialSerializer(source='material', many=True)
    theme_char = OptionsThemeSerializer(source='theme', many=True)

    class Meta:
        model = Live
        fields = ['label', 'streamer_pseudo', 'theme_char', 'start_date', 'end_date', 'pegi', 'material_char']
