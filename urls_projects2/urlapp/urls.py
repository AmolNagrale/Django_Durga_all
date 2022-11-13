from django.contrib import admin
from urlapp import views
from django.urls import path

urlpatterns = [
    path('hydjobs/', views.hydjobsinfo),
    path('punejobs/', views.punejobsinfo),
    path('mumbaijobs/', views.mumbaijobsinfo),
    path('noidajobs/', views.noidajobsinfo),
]


