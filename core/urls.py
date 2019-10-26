from django.urls import include, path, re_path
from cuser.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', LoginView.as_view(authentication_form=AuthenticationForm), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('activate/<uidb64>[0-9A-Za-z_]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/',
        views.activate, name='activate'),
    path('', views.homepage, name='homepage'),
]
