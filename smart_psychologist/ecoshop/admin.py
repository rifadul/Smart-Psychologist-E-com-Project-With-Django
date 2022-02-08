from django.contrib import admin
from .models import ProductCategory,ProductDetails,Cart,OrderPlaced
# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['id','product_category']




@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_price','discount_price','product_category','product_description','product_image']


@admin.register(Cart)
class CardAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','address','payment_method','orderdate','status']