from django.urls import include, path, re_path
from cuser.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordResetView
from . import views

urlpatterns = [
    path('test/', views.tester, name='test'),
    path('s/', include('app_static_pages.urls')),
    path('t/', include('app_teachers.urls')),
    path('profile/', views.profile, name='profile'),
    path('new_social/', views.new_social, name='new_social'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', LoginView.as_view(authentication_form=AuthenticationForm), name='login'),
    path('accounts/password_reset/', PasswordResetView.as_view(html_email_template_name="email/password_reset_email.html",
        subject_template_name="email/password_reset_subject.txt"), name='password_reset'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('activate/<uidb64>[0-9A-Za-z_]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/',
        views.activate, name='activate'),
    path('', views.homepage, name='homepage'),
]
