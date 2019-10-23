from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]
