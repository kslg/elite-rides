from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


"""
inline item is going to allow us to add and edit line items in the admin
right from inside the order model.
When we look at an order. We'll see a list of editable line items
on the same page. Rather than having to go to the order line item interface.
"""


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)


"""
readonly_fields:
These fields are all things that will be calculated
by our model methods. We don't want anyone to have the ability to edit them
since it could compromise the integrity of an order.
"""

"""
fields:
Allow us to specify the order of the fields in the admin interface
which would otherwise be adjusted by django, due to the use of
some read-only fields. This way the order stays the same as it
appears in the model.
"""

"""
list_display:
To restrict the columns that show up in the order list to only a few key items.
Set them to be ordered by date in reverse chronological order
putting the most recent orders at the top.
"""
