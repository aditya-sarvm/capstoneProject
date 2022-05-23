from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createMostPopular', views.createRecommendations, name='createMostPopular'),
    path('getMostPopular', views.getMostPopular, name='getMostPopular'),
    path('updateMostPopular', views.updateMostPopular, name='updateMostPopular'),
    path('deleteMostPopular', views.deleteMostPopular, name='deleteMostPopular'),
]