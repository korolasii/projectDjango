from django.contrib import admin
from .models import Order, OrderProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created', 'updated']
    list_filter = ['user', 'status', 'created', 'updated']
    list_editable = ['status']    
    search_fields = ['id', 'user', 'status', 'created', 'updated']
    
@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']
    list_filter = ['order', 'product', 'price', 'quantity']
    list_editable = ['price', 'quantity']    
    search_fields = ['id', 'order', 'product', 'price', 'quantity']