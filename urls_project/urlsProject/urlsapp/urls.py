from django.contrib import admin
from django.urls import path
from urlsapp import views

urlpatterns = [
    path('hydjobs/', views.hydjobsinfo),
    path('punejobs/', views.punejobsinfo),
    path('mumbaijobs/', views.mumbaijobsinfo),
    path('noidajobs/', views.noidajobsinfo),
]