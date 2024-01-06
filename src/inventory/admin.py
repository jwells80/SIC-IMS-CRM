from django.contrib import admin

from .models import (
    Category,
    Item,
)


class ItemInline(admin.StackedInline):
    model = Item
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
