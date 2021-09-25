from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('auth-login/', views.LoginView, name = 'auth-login'),
    path('auth-register/', views.RegisterEmployee, name = 'auth-register'),
    path('auth-logout/', views.LogoutView, name = 'auth-logout'),
    path('auth-change-password/', views.ChangePasswordView, name = 'auth-change-password'),
]
