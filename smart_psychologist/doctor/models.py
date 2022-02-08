from django.db import models

# Create your models here.
class DoctorCategory(models.Model):
    specialist_sector = models.CharField(max_length=30)

    def __str__(self):
        return (self.specialist_sector)

class DoctorInformation(models.Model):
    full_name = models.CharField(max_length=100)
    specialist_sector = models.ForeignKey(DoctorCategory, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    about_me = models.TextField(max_length=1000)
    chamber_address = models.TextField(max_length=1000) 
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    doctor_image = models.ImageField(upload_to='uploads/doctor_images/', blank=True, null=True)

    # def __str__(self):
    #     return self.headline

    # class Meta:
    #     ordering = ['headline']