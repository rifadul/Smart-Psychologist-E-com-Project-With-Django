from django.shortcuts import render
from .models import SmartBlog

# Create your views here.
def blog(request):
    all_posts = SmartBlog.objects.all()
    return render(request,'blog/blog.html',{'blog_active':'navbar-active-color','posts':all_posts})

def blogDetails(request, slug):
    post = SmartBlog.objects.get(slug=slug)
    return render(request, 'blog/blogdetails.html', {'blog_active':'navbar-active-color','post': post})
