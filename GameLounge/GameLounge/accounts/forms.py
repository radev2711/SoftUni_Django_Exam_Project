from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ProfileModel


class CreateProfileForm(UserCreationForm):
    # consent_to_terms_and_conditions = forms.BooleanField()

    class Meta:
        model = ProfileModel
        fields = ('email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('nickname', 'age')
