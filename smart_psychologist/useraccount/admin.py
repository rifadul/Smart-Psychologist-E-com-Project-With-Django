from django.contrib import admin
from .models import Customer,DeliveryAddress


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','name','phone_number','address','division','city','zip_code','profile_image']


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display=['id','user','home_address','division','district','city','zip_code']
