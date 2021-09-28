from django.urls import path
from . import views

app_name = 'leave'


urlpatterns = [
    path('apply-leave', views.apply_leave, name = 'apply-leave'),
    path('approve-leave/<str:id>', views.approve_leave, name  = 'approve-leave'),
    path('decline-leave/<str:id>', views.decline_leave, name = 'decline-leave'),
]
