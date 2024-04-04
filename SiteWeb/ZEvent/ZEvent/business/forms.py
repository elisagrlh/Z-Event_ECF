from django import forms

class CreateUserForm(forms.Form):
    email = forms.EmailField(label='Adresse Email')