from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('auth-login/', views.LoginView, name = 'auth-login'),
    path('auth-register/', views.RegisterEmployee, name = 'auth-register'),
    path('auth-logout/', views.LogoutView, name = 'auth-logout'),
    path('auth-change-password/', views.ChangePasswordView, name = 'auth-change-password'),

    path('all-employees', views.allEmployees, name = 'all-employes'),
    path('edit-employee/<str:id>', views.editEmployee, name = 'edit-employee'),
    path('edit-profile/<str:id>', views.editUserProfile, name = 'edit-user-profile'),
    path('delete-employee/<str:id>', views.deleteEmployee, name = 'delete-employee'),
    path('change-password/<str:id>', views.ChangePasswordView, name = 'change-password')

]
