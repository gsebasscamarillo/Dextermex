from django.urls import path
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'', views.index),
    url(r'^()/$', views.rastrear, name = 'rastrear'),
]