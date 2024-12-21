from django.contrib import admin
from .models import Category, Product, Cart, CartItem

# Registering Category, Cart, and CartItem models
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)

# Registering Product model with custom admin configuration
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'slug')
    prepopulated_fields = {'slug': ('name',)}
