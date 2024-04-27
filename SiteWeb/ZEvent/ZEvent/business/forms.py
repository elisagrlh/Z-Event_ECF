from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import UserData
from .models import Live




class CreateUserForm(forms.ModelForm):
    #age = forms.IntegerField(min_value=0)

    class Meta:
        model = User    
        fields = ['email', 'first_name', 'last_name', "username"]

        labels = {
            'email': 'Adresse email',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'username': 'Nom d’utilisateur',
        }


class AgeForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['age']

        labels = {'Age': 'age'}





class MultiSelectForm(forms.ModelForm):
   class Meta:
       model = Live
       fields = ["label", "streamer_name", "theme", "start_date", "end_date", "pegi", "material"]
       widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'options': forms.SelectMultiple(attrs={'class': 'my-multiselect-class'}),
            'theme': forms.CheckboxSelectMultiple(attrs={'class': 'multiSelection'}),
            'material': forms.CheckboxSelectMultiple(attrs={'class': 'multiSelection'}),
        }
       
       labels = {
            'label': 'Libellé',
            'streamer_name': 'Streamer',
            'theme': 'Thème',
            'start_date': 'Date et heure de début',
            'end_date': 'Date et heure de fin',
            'pegi': 'PEGI',
            'material': 'Matériel'
        }
       
       def __init__(self, *args, **kwargs):
        super(Live, self).__init__(*args, **kwargs)
        self.fields['start_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_date'].input_formats = ('%Y-%m-%dT%H:%M',)












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