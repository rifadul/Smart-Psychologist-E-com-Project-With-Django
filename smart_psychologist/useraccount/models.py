from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    phone_number = models.CharField(max_length=20,default='')
    address = models.CharField(max_length=100,default='')
    division = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    zip_code = models.IntegerField(null=True)
    profile_image = models.ImageField(upload_to='uploads/profile_images/', blank=True, null=True)

    def __str__(self):
        return str(self.user)


class DeliveryAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    home_address = models.CharField(max_length=100,default='')
    division = models.CharField(max_length=100,default='')
    district = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    zip_code = models.IntegerField(null=True)

    def __str__(self):
        return str(self.city)
