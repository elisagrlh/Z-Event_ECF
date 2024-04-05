from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class CreateUserForm(forms.ModelForm):
    age = forms.IntegerField(min_value=0)

    class Meta:
        model = User
        fields = ['email', 'age', 'first_name', 'last_name', "username"]

        labels = {
            'email': 'Adresse email',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'username': 'Nom d’utilisateur',
            'age': 'Age',
        }
