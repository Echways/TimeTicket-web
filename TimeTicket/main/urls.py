from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views
from .views import *

urlpatterns = [
    path('', views.all_event, name='main'),
    path('account/profile/', ProfileView.as_view(), name='profileview'),
    path('account/signup/', UserRegView.as_view(), name='signup'),
    # path('account/login/', UserLoginView.as_view(), name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('reg_event', views.reg_event, name='reg_event')
]