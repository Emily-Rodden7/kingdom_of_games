from django.contrib import admin
from .models import Product, Category, Review, Wishlist
from .models import GiftCard

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

@admin.register(GiftCard)
class GiftCardAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'issued_to', 'is_used', 'issued_on')
    search_fields = ('code', 'issued_to__username')
    list_filter = ('is_used',)  

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
admin.site.register(Wishlist)

