from django.contrib import admin

from SuperMarketApi.models import Category, Item, SubCategory

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'subcategory', 'amount']
