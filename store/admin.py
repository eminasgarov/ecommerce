from django.contrib import admin
from django.contrib.admin.decorators import display
from django.utils.html import format_html
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px" />'.format(object.images.url))

    list_display            = ('thumbnail', 'product_name', 'category', 'price', 'stock', 'modified_date', 'is_available')
    list_display_links      = ('thumbnail', 'product_name')
    prepopulated_fields     = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)