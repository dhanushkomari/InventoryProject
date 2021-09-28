from django.contrib import admin
from .models import Leave

# Register your models here.

class LeaveAdmin(admin.ModelAdmin):
    list_display = ['leave_id', 'user', 'from_date', 'to_date', 'status']
    list_per_page = 20
admin.site.register(Leave, LeaveAdmin)