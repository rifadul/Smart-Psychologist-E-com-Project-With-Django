from django.db import models
from django.utils.text import slugify

# Create your models here.

class SmartBlog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500,unique=True)
    description = models.TextField()
    blogImage = models.ImageField(upload_to='uploads/blog_images/', blank=True, null=True)
    uploadDate = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title,allow_uni)
    #     super(SmartBlog, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title,allow_unicode=True)
        super().save(*args, **kwargs)