from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('search/', views.teachers, name="teachers"),
    path('my_panel/', views.teacher_panel, name="teacher_panel"),
    path('start/', views.start_teaching, name="start_teaching"),
    path('single_teacher/<int:pk>/', views.single_teacher, name="single_teacher"),
]
