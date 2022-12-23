from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'contact_number',
        'order_number',
        'message'
    )

    ordering = ('full_name', 'order_number')


admin.site.register(Contact)
