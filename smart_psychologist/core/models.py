from django.db import models

# Create your models here.
class ContactAdd(models.Model):
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __iter__(self):
        return iter(self.__dict__.items())
    