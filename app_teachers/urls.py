from django.contrib import admin
from django.urls import include, path
from . import views, views_ajax

urlpatterns = [
    path('search/', views.teachers, name="teachers"),
    path('my_panel/', views.teacher_panel, name="teacher_panel"),
    path('start/', views.start_teaching, name="start_teaching"),
    path('favourites/', views.favourites, name="favourites"),
    path('single_teacher/<int:pk>/', views.single_teacher, name="single_teacher"),
    path('single_lesson/<int:pk>/', views.single_lesson, name="single_lesson"),

    # ones for teacher related ajax calls:
    path('ajax/accept_lesson/', views_ajax.accept_lesson, name="accept_lesson"),
    path('ajax/reject_lesson/', views_ajax.reject_lesson, name="reject_lesson"),
]
