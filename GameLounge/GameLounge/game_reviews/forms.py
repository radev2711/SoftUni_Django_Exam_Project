from django import forms
from .models import ReviewModel, RateGameModel


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['text']
        labels = {
            'text': ''
        }
        widgets = {
            'text': forms.Textarea(
                attrs={'placeholder': 'Enter review here...'}
            )
        }


class RateGameForm(forms.ModelForm):
    class Meta:
        model = RateGameModel
        fields= ['rating']
