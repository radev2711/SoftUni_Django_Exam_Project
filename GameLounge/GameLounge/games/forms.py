from django import forms
from .models import GameModel


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'
        exclude = ['rating']


class SearchForGameForm(forms.Form):
    title_string = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search for game title'}))
