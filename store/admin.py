from django.contrib import admin
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Products


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'password')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'price', 'address', 'phone', 'date', 'status')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Products, ProductAdmin)
