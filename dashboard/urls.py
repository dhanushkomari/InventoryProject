from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('user/<str:id>', views.user_dashboard, name = 'user-dashboard'),
    path('admin/', views.admin_dashboard,  name = 'admin-dashboard'),
    
]
