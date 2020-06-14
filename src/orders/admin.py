from django.contrib import admin
from django.conf.urls import url

from .models import Order
from .services import return_money
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product_id',
        'start_date',
        'status',
    )
    
    readonly_fields = (
        'product',
        'status',
    )
    
    ordering = ('status', '-start_date',)
    
    def save_model(self, request, obj, form, change):
        if obj.status == Order.STATUS_PAID and obj.return_date is not None:
            assert obj.damage_cost_tomans is not None
            obj.status = Order.STATUS_RETURNED
            super().save_model(request, obj, form, change)
            return_money(obj)
        else:
            super().save_model(request, obj, form, change)