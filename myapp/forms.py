from django import forms
from .models import UserProfile

class userForm(forms.ModelForm):
    class Meta:
        model =UserProfile
        fields='__all__'
