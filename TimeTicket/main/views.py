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


class ProfileView(ListView):
    model = Event
    template_name = 'profileview.html'


def register(request):
    if request.method == 'GET':
        form = SignUp()
        context = {'form': form}
        return render(request, 'profileadd.html', context)

    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            userid = form.cleaned_data.get('username')
            return render(request, 'profileview.html', {'profiledata': User.objects.all().filter(username=userid)})
        else:
            print('Form is not valid')
            context = {'form': form}
            return render(request, 'profileadd.html', context)
    return render(request, 'profileadd.html', {})
