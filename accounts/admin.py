from django.contrib import admin
from .models import CustomUser as User
from .models import Department
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','employee_id', 'username', 'department', ]
    list_per_page = 20
admin.site.register(User, UserAdmin)

admin.site.register(Department)
 

