from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'time_added')


admin.site.register(Order, OrderAdmin)
