from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('exams/', views.exams, name="exams"),
]
