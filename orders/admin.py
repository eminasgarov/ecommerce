from asyncio.format_helpers import extract_stack
from pyexpat import model
from re import search
from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Payment, Order, OrderProduct

# Register your models here.

class OrderProductInline(admin.TabularInline):
    model           = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'variation', 'quantity', 'product_price', 'ordered')
    extra           = 0

class OrderAdmin(admin.ModelAdmin):
    list_display    = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'status', 'is_ordered', 'created_at']
    list_filter     = ['status', 'is_ordered']
    search_fields   = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page   = 20
    inlines         = [OrderProductInline]
    
class PaymentAdmin(admin.ModelAdmin):
    list_display    = ['payment_id', 'user', 'payment_method', 'amount_paid', 'status', 'created_at']
    list_filter     = ['payment_method', 'status']
    search_fields   = ['payment_method', 'status', 'payment_id', 'user']
    list_per_page   = 20

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)