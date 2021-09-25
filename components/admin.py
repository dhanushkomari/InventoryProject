from django.contrib import admin
from .models import ComponentCategory,Component

# Register your models here.

class ComponentAdmin(admin.ModelAdmin):
    list_display = ['component_id','name', 'category','stock', 'avialable','component_location']
    list_editable = ['stock',]
    # prepopulated_fields = {'slug':('name',)}
admin.site.register(Component, ComponentAdmin)

class ComponentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    # prepopulated_fields = {'slug':('name',)}
admin.site.register(ComponentCategory, ComponentCategoryAdmin)

