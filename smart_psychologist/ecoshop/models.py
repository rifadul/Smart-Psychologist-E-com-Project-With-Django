from django.db import models
from django.contrib.auth.models import User
from useraccount.models import Customer,DeliveryAddress

# Create your models here.
class ProductCategory(models.Model):
    product_category = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.product_category


class ProductDetails(models.Model):
    product_name = models.CharField(max_length=100,default='')
    product_price = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(blank=True,null=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    # product_sub_category = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE,default='')
    product_description = models.TextField(max_length=1000,default='')
    product_image = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)
    
    
    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.user)

    @property   
    def total_cost(self):
        if self.product.discount_price:
            price = self.product.discount_price
        else:
            price = self.product.product_price
        return self.quantity * price


STATUS_CHOICES={
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
}


class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    address = models.ForeignKey(DeliveryAddress,on_delete=models.CASCADE,default='')
    payment_method = models.CharField(max_length=200,default='')
    orderdate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100 ,choices=STATUS_CHOICES,default='Pending')

    @property   
    def total_cost(self):
        if self.product.discount_price:
            price = self.product.discount_price
        else:
            price = self.product.product_price
        return self.quantity * price
