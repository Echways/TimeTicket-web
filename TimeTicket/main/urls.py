from django.urls import path, include
from django.contrib import admin

from . import views
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('account/profile/', ProfileView.as_view(), name='profileview'),
    path('account/signup/', views.register, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
]