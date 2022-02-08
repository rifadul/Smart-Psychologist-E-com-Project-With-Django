from django.contrib import admin
from .models import DoctorCategory,DoctorInformation
# Register your models here.

@admin.register(DoctorCategory)
class DoctorCategoryAdmin(admin.ModelAdmin):
    list_display=['id','specialist_sector']



@admin.register(DoctorInformation)
class DoctorInformationAdmin(admin.ModelAdmin):
    list_display=['id','full_name','specialist_sector','designation','about_me','chamber_address','phone_number','email','doctor_image']
    list_per_page = 5

