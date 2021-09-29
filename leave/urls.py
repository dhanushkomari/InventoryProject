from django.urls import path
from . import views

app_name = 'leave'


urlpatterns = [
    path('apply-leave', views.apply_leave, name = 'apply-leave'),
    path('all-leaves-list', views.leave_list_admin, name = 'all-leaves'),
    path('user-leaves-list/<str:username>', views.leaves_list_user, name = 'user-leaves'),
    path('leave-detail-admin/<str:id>', views.leave_detail_admin, name = 'leave-detail-admin'),
    path('approve-leave/<str:id>', views.approve_leave, name  = 'approve-leave'),
    path('decline-leave/<str:id>', views.decline_leave, name = 'decline-leave'),
]
