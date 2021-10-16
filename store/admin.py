from django.contrib import admin
from store.models import Category, Product, Cart, CartItem, Order, OrderItem, OrderStatus, Promotion
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price',
                    'stock', 'created_at', 'updated_at']
    list_editable = ['price', 'stock']
    list_per_page = 10


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'total',
                    'token', 'created_at', 'updated_at']
    list_per_page = 10


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'created_at', 'updated_at']
    list_per_page = 10


admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Promotion)
admin.site.register(CartItem)
admin.site.register(OrderStatus)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
