from django.contrib import admin
from .models import SmartBlog

# Register your models here.
@admin.register(SmartBlog)
class SmartBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug',
                    'description', 'blogImage', 'uploadDate']