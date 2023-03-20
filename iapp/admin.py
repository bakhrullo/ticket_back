from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'tg_id', 'user_phone', 'created_date']
    list_filter = ['id', 'user_name', 'tg_id', 'user_phone', 'created_date']
    search_fields = ['user_name',  'tg_id', 'user_phone']


class SectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity', 'beg_price', 'end_price','get_image']
    list_filter = ['name', 'created_date', 'beg_price', 'end_price',]
    list_editable = ['name', 'quantity', 'beg_price', 'end_price']
    search_fields = ['name']
    fields = ['name', 'image', 'quantity']
    readonly_fields = ['created_date']

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_image.short_description = 'Rasim'


class RowAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sector', 'quantity', 'created_date']
    list_filter = ['name', 'sector', 'created_date']
    list_editable = ['name', 'sector', 'quantity']
    search_fields = ['name']


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'row', 'status', 'price']
    list_filter = ['name', 'price', 'created_date']
    list_editable = ['name', 'row', 'price', 'status']
    search_fields = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'pay_type', 'total_price']
    list_filter = ['user', 'pay_type', 'total_price', 'created_date']
    search_fields = ['total_price']


class CallsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone']
    list_editable = ['phone']


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'update_date']
    list_editable = ['text']

    def has_delete_permission(self, request, obj=None):
        return False

    # def has_add_permission(self, request):
    #     return False


admin.site.unregister(Group)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Row, RowAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Calls, CallsAdmin)


admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel'
