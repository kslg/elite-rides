from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category


class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'sku',
        'name',
        'make',
        'model',
        'category',
        'price',
        'image',
    )
    summernote_fields = ('description')

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
