from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('account/profile/', ProfileView.as_view(), name='profileview'),
    path('account/signup/', UserRegView.as_view(), name='signup'),
    # path('account/login/', UserLoginView.as_view(), name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('reg_event', views.reg_event, name='reg_event'),
    path('pdf/<int:pk>/', views.pdf_e, name='pdf_e'),
    path('account/passwordchange/', views.change_password, name='passwordchange'),
    path('account/profile/events/', ProfileEventsView.as_view(), name='profileevents'),
    path('account/profile/events/videos/', ProfileEventVideosView.as_view(), name='profileeventvideos'),
]