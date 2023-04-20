from django.urls import path, include
from django.contrib import admin

from . import views
from .views import *

urlpatterns = [
    path('', views.all_event, name='main'),
    path('account/profile/', ProfileView.as_view(), name='profileview'),
    path('account/signup/', views.register, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('reg_event', views.reg_event, name='reg_event')
]