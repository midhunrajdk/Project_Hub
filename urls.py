from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('pdash/', views.pdash, name='pdash'),

]