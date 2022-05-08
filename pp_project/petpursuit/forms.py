from django import forms
from .models import State, Shelter, Canine, Feline, User

class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = ('stateName',)

class ShelterForm(forms.ModelForm):

    class Meta:
        model = Shelter
        fields = ('shelterName', 'state', 'website',)

class CanineForm(forms.ModelForm):

    class Meta:
        model = Canine
        fields = ('dogName', 'breed', 'age', 'shelter', 'photo_url',)

class FelineForm(forms.ModelForm):

    class Meta:
        model = Feline
        fields = ('catName', 'breed', 'age', 'shelter', 'photo_url',)

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('userName', 'email', 'password',)