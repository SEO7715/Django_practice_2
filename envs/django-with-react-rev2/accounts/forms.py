from django import forms
from .models import User

class SignupForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']