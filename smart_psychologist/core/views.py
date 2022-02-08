from django.shortcuts import render
from django.views import View
from ecoshop.models import Cart,ProductDetails

# Create your views here.

def home(request):
    return render(request, 'core/home.html',{'home_active':'navbar-active-color'})