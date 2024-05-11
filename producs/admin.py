from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        return obj.photo.url if obj.photo else None

    photo_preview.short_description = 'Photo Preview'
