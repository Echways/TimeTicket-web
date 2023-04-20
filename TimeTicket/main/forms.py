from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *

from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    middle_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    mobilephone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = NewUser
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'email', 'mobilephone')


class EventRegForm(forms.ModelForm):
    class Meta:
        model = RegisterEvent
        fields = ['name', 'surname', 'email', 'event_id']









