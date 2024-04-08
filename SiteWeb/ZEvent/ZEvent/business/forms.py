from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import UserData




class CreateUserForm(forms.ModelForm):
    age = forms.IntegerField(min_value=0)

    class Meta:
        model = User    
        fields = ['email', 'first_name', 'last_name', "username"]

        labels = {
            'email': 'Adresse email',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'username': 'Nom d’utilisateur',
            'age': 'Age',
        }


'''
class CreateUserForm(UserCreationForm):
    age = forms.IntegerField(min_value=0, label="Âge")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'age']
        labels = {
            'email': 'Adresse email',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'username': 'Nom d’utilisateur',
        }

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        User.age = self.cleaned_data["age"]
        if commit:
            user.save() 
        return user

'''