from django.contrib import admin
from .models import Product, Category, Warranty

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'make',
        'model',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class WarrantyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Warranty, WarrantyAdmin)
