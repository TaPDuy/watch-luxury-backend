from django.contrib import admin

from .models import Product, Category

admin.site.register(Product)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Category, CategoryAdmin)
