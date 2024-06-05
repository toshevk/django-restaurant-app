from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "category", "status", "price")
    list_filter = ("status",)
    search_fields = ("meal", "description")
    ordering = ("-category",)


admin.site.register(Item, MenuItemAdmin)
