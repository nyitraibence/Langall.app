from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('start/', views.start_teaching, name="start_teaching"),
    path('search/', views.teachers, name="teachers"),
]
