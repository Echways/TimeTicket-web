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
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



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
    success_url = '../../account/profile/'


def plural_days(n):
    """ Склонение день/дней/дня """
    days = ['день', 'дня', 'дней']
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2
    return str(n) + ' ' + days[p]


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    hostnameclean = ' '.join(str(event.hostname).replace('_', '-').split('-'))
    q = event.eventstartday - datetime.datetime.now(datetime.timezone.utc)
    q = str(q).split()
    st = int(q[0]) + 1
    if st > 0:
        start_event = plural_days(st)
    elif st == 0:
        start_event = 'Сегодня'
    else:
        start_event = 'Мероприятие прошло'
    return render(request, 'event_detail.html', {'event': event, 'start_event': start_event, 'hostname':hostnameclean})


def reg_event(request):
    if request.method == 'POST':
        form = EventRegForm(request.POST)
        if form.is_valid():
            ev = form.save(commit=False)
            #print(ev.event_id_id)
            obj = Event.objects.get(pk=ev.event_id_id)
            #manaprint(obj.eventname)

            to = ev.email
            msg = MIMEMultipart()
            msg['From'] = 'kavantnntechnostrelka2023@gmail.com'
            msg['To'] = to
            msg['Subject'] = 'Hi'

            text = MIMEText('hi')
            msg.attach(text)

            with open(f'C:/Users/alexs/PycharmProject/nn202343/TimeTicket{obj.ticket.url}', 'rb') as f:
                image = MIMEImage(f.read())
                msg.attach(image)

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login('kavantnntechnostrelka2023@gmail.com', 'pobqesmqlozlimde')
                smtp.send_message(msg)

            ev.save()
            return redirect('reg_event')
    else:
        form = EventRegForm()
    return render(request, 'reg_event.html', {'form': form})






