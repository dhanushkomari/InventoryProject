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
    path('change-password/<str:id>', views.ChangePasswordView, name = 'change-password'),

    path('add-department/', views.create_dept, name = 'create-dept'),
    path('update-dept/<str:id>', views.update_dept, name = 'update-dept'),
    path('delete-dept/<str:id>', views.delete_dept, name = 'delete-dept'),
    path('all-depts', views.dept_list, name = 'all-depts'),

]
