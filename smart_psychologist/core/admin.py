from django.contrib import admin
from .models import ContactAdd

# Register your models here.
@admin.register(ContactAdd)
class ContactFormAdmin(admin.ModelAdmin):
    list_display=['id','full_name','subject','email','message']
