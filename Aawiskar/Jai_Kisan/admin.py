from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer,
    Product,
    Item,
    Booked,
    Vendor,
    Farmer,
    VendorProduct,
    Contact,
)

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['msg_id','name','email','desc']


@admin.register(Farmer)
class FarmerModelAdmin(admin.ModelAdmin):
    list_display = ['User_name', 'First_name', 'Last_name', 'email','state' ,'city','locality', 'zipcode','password' ]



@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category',
                    'product_image', 'vendor_name', 'vendor_location', 'capacity', 'features', 'flight_time', 'drone_range']



@admin.register(Item)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'duration']
    
@admin.register(Vendor)
class VendorModelAdmin(admin.ModelAdmin):
    list_display = ['User_name', 'First_name', 'Last_name', 'email','state' ,'city','locality', 'zipcode','password' ]

@admin.register(VendorProduct)
class VendorProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','product','user','brand','category']


@admin.register(Booked)
class BookedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product','duration', 'ordered_date',
                    'status']

    # def product_info(self, obj):
    #     link = reverse("admin:app_product_change", args=[obj.product.pk])
    #     return format_html('<a href="{}">{}</a>', link, obj.product.title)

    # def customer_info(self, obj):
    #     link = reverse("admin:app_customer_change", args=[obj.customer.pk])
    #     return format_html('<a href="{}">{}</a>', link, obj.customer.name)


