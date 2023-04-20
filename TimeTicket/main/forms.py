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

    name = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class':'form-control'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    event_id = forms.CharField(max_length=50)
    ticket_id = forms.CharField(max_length=5)

    class Meta:
        model = RegisterEvent
        fields = ['name', 'surname', 'email', 'event_id', 'ticket_id']

    def __init__(self, *args, **kwargs):
        TICKET_CHOICES = (
            (1, "Билет 'Standard'"),
            (2, "Билет с обедом"),
            (3, "Билет с кофе"),
            (4, "Билет 'VIP'"),
        )
        super(EventRegForm, self).__init__(*args, **kwargs)
        self.fields['event_id'] = forms.ModelChoiceField(queryset=Event.objects.all(), widget=forms.Select(attrs={'class':'select-purchase'}))
        self.fields['ticket_id'] = forms.ChoiceField(choices=TICKET_CHOICES, widget=forms.Select(attrs={'class':'select-purchase'}))






