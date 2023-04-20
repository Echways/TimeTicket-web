from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.edit import UpdateView
from django.views.decorators.http import require_http_methods
from itertools import chain
from .models import *
from .forms import *


class MainView(ListView):
    model = Event
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = {'Eventlist': Event.objects.all()}
        return context


class ProfileView(ListView):
    model = Event
    template_name = 'profileview.html'

# class UserLoginView(CreateView):
#     form_class = LoginForm
#     template_name = 'registration/login.html'

class UserRegView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    # success_url = '../../account/profile/'
