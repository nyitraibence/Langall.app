from django.urls import include, path
from cuser.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('accounts/login/', LoginView.as_view(authentication_form=AuthenticationForm), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.homepage, name='homepage'),
]
