from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer,
    Product,
    Item,
    Booked,
)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category',
                    'product_image']


@admin.register(Item)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'duration']


@admin.register(Booked)
class BookedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product','product_info','customer_info','duration', 'ordered_date',
                    'status']

    def product_info(self, obj):
        link = reverse("admin:Jai_Kisan_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def customer_info(self, obj):
        link = reverse("admin:Jai_Kisan_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)


