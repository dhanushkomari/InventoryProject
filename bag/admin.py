from django.contrib import admin
from .models import Bag, BagItem

# Register your models here.


class BagAdmin(admin.ModelAdmin):
    list_display = ['bag_id', 'created_at']
    list_per_page = 20
admin.site.register(Bag, BagAdmin)



class BagItemAdmin(admin.ModelAdmin):
    list_display = ['component', 'bag']
    list_per_page = 20
admin.site.register(BagItem, BagItemAdmin)
