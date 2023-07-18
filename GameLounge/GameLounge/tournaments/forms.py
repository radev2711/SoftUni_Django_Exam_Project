from django import forms
from .models import TournamentModel


class TournamentCreateForm(forms.ModelForm):
    class Meta:
        model = TournamentModel
        fields = '__all__'
        exclude = ['participants']

        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
