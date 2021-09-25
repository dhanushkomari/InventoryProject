from django.contrib import admin
from .models import Order, OrderItem, Deployment, DeployedItems

class OrderItemAdmin(admin.ModelAdmin):
    list_per_page = 20
admin.site.register(OrderItem, OrderItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'username', 'email', 'created_at', 'status']
    list_per_page = 20
admin.site.register(Order, OrderAdmin)


class DeploymentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['deployment_id', 'username', 'email', 'created_at']

admin.site.register(Deployment, DeploymentAdmin)

class DeployedItemsAdmin(admin.ModelAdmin):
    list_display = ['deployment', 'component', 'deployed_by', 'deployed_into', 'quantity']
    list_per_page = 20
admin.site.register(DeployedItems, DeployedItemsAdmin)
