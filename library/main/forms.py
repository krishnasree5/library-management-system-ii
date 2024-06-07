from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
				'placeholder': 'Your Username',
	}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
				'placeholder': 'Your Email address',
	}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
				'placeholder': 'Your Password',
	}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
				'placeholder': 'Retype Password',
	}))
