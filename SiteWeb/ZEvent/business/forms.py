from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import UserData
from .models import Live
from .models import LiveRegistration


class CreateUserForm(forms.ModelForm):
    #age = forms.IntegerField(min_value=0)
    first_name = forms.CharField(required=True, max_length=60)
    last_name = forms.CharField(required=True, max_length=60)
    class Meta:
        model = User    
        fields = ['email', 'first_name', 'last_name', "username"]

        labels = {
            'email': 'Adresse email',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'username': 'Nom d’utilisateur',
        }


class AddInfoForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['age', "pseudo"]
        labels = {
           'Age': 'age',
            'Pseudo': 'pseudo'
        }





class MultiSelectForm(forms.ModelForm):
   class Meta:
       model = Live
       fields = ["label", "streamer_pseudo", "theme", "start_date", "end_date", "pegi", "material"]
       widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            #'options': forms.SelectMultiple(attrs={'class': 'my-multiselect-class'}),
            'theme': forms.CheckboxSelectMultiple(attrs={'class': 'multiSelection'}),
            'material': forms.SelectMultiple(attrs={'class': 'multiSelection'}),
        }
       
       labels = {
            'label': 'Libellé',
            'streamer_pseudo': 'Streamer pseudo',
            'theme': 'Thème',
            'start_date': 'Date et heure de début',
            'end_date': 'Date et heure de fin',
            'pegi': 'PEGI',
            'material': 'Matériel (ctrl multisélection)',

        }
       
       def __init__(self, *args, **kwargs):
        super(Live, self).__init__(*args, **kwargs)
        self.fields['start_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_date'].input_formats = ('%Y-%m-%dT%H:%M',)






class LiveRegistrationForm(forms.ModelForm):
    class Meta:
      model = LiveRegistration
      fields = ["email"]
      labels = {
       "email": "Adresse email"
        }