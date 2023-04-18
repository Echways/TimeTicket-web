from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic.edit import UpdateView
from django.views.decorators.http import require_http_methods
from itertools import chain
from .models import *

class MainView(ListView):
    model = Event
    template_name = 'govno.html'