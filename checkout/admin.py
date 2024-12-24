from django.contrib import admin

from .models import Order,Order_item


class OrderAdmin(admin.ModelAdmin):
    list_display = ('username','email','full_name')
    list_editable = ('full_name',)
    list_per_page = 4
    # search_fields = ('username',)

# Register your models here.
admin.site.register(Order,OrderAdmin)
admin.site.register(Order_item)