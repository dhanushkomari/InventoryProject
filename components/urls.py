from django.urls import path
from . import views

app_name = 'components'

urlpatterns = [
    path('',views.ComponentListView, name = 'component-list-all'),  
    path('<str:id>/', views.CatComponentListView, name =  'component-list-cat'),
    
    path('category/all', views.all_categories, name = 'all-categories'),
    path('add/category', views.add_category, name = 'add-category'),
    path('update/category/<str:id>', views.update_category, name = 'update-category'),
    path('delete/category/<str:id>', views.delete_category, name='delete-category'),
    path('detail/component/<str:id>', views.detailed_component, name = 'component-detail'),


    path('admin/all', views.allcomponents, name = 'all-components-admin'),
    path('admin/add-component', views.add_component, name = 'add-component'),
    path('admin/update-component/<str:id>', views.update_component, name = 'update-component'),
    path('admin/delete-component/<str:id>', views.delete_component, name = 'delete-component'),

]
