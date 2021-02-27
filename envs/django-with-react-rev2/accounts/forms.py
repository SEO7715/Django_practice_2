from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm
)
from .models import User

# class SignupForm(forms.ModelForm):
    # class Meta:
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password']