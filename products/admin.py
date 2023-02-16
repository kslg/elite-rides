from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category, Reviews


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


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'date_added',
        'customer_name',
        'product',
    )

    ordering = ('date_added',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews, ReviewsAdmin)
