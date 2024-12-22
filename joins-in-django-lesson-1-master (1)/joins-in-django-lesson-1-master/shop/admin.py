from django.contrib import admin
from shop.models import Category, Item, Tag, Image
from django.contrib.contenttypes.admin import GenericTabularInline

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0

class TagInline(admin.StackedInline):
    model = Item.tags.through
    extra = 0

class ImageInline(GenericTabularInline):
    model = Image
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    ordering = ['name']
    inlines = [ItemInline, ImageInline]


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description']
    search_fields = ['name', 'description']
    ordering = ['-price']
    inlines = [TagInline, ImageInline]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)