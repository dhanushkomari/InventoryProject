from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('success/', views.order_success, name = 'order_success'),
    path('orders/', views.user_orders, name = 'user-orders'),
    path('order-detail/<str:id>', views.order_detail, name = 'order-detail'),
    path('order-detail-admin/<str:id>', views.order_detail_admin, name='order-detail-admin'),
    path('all-orders/', views.all_order, name = 'all-orders'),  
    path('order-accept/<str:id>/', views.order_accept, name = 'order-accept'),
    path('order-decline/<str:id>', views.order_decline, name = 'order-decline'),
    path('order-return/<str:id>', views.order_return, name = 'order-return'),
    path('order-deploy/<str:id>', views.order_deploy, name = 'order-deploy'),
    # path('deploy-details', views.deploy_details, name = 'deploy-details-post'),

    path('deploy-list/admin', views.deployed_list_admin, name = 'admin-deploy-list'),
    path('deploy-list/user/<str:id>', views.deployed_list_user, name = 'user-deploy-list'),

    path('deploy-detail/<str:id>', views.deployed_detail, name = 'deploy-detail')
]
