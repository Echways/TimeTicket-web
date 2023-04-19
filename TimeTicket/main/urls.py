from django.urls import path
from .views import *

urlpatterns = [
    path('', get_list_event, name='index'),
    #path('profile/', MainView.as_view(), name='main'),
    #path('profile/', MainView.as_view(), name='main'),
]
