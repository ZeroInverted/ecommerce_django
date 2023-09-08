from django import forms
from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'password1',
                  'password2', 'phone', 'adress']
        # Add placeholder to inform user that the email will be used as a username
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'will be used as your username'}),
        }
