from django.urls import path
from . import views

app_name = 'bag'

urlpatterns = [
    path('add-to-bag/<str:component_id>', views.add_to_bag, name = 'add_to_bag'),
    path('bag-details/', views.bag_details, name = 'bag_details'),
    path('remove-item/<str:component_id>', views.remove_item, name = 'remove-item'),
    path('delete-item/<str:component_id>', views.delete_bag_items, name = 'delete-items'),
    path('request-components', views.request_components, name = 'request_components')
]
