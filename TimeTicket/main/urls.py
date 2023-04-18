from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('profile/', MainView.as_view(), name='main'),
    path('profile/', MainView.as_view(), name='main'),
]
