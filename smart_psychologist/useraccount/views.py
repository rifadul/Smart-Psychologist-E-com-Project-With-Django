from django.shortcuts import render, HttpResponseRedirect, redirect
from .form import UserSingupForm, UserLoginForm, CustomerProfileForm, DeliveryAddressForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib.auth.models import User
from .models import Customer, DeliveryAddress


# Create your views here.

class UserRegistration(View): 
    def get(self, request): 
        if not request.user.is_authenticated: 
            forms = UserSingupForm() 
            return render(request,'useraccount/signup.html', {'regi_active': 'navbar-active-color', 'forms':
            forms}) 
        else: return HttpResponseRedirect('/')

    def post(self, request):
        forms = UserSingupForm(request.POST)
        if forms.is_valid():
            messages.success(
                request, 'Account Create Successfully! Please Login.')
            forms.save()
            # forms = UserSingupForm()
            return redirect('/account/login/')
        return render(request, 'useraccount/signup.html', {'regi_active': 'navbar-active-color', 'forms': forms})


class UserProfile(View):
    def get(self, request):
        customar_profile = Customer.objects.filter(user=request.user)
        return render(request, 'useraccount/profile.html', {'user_active': 'navbar-active-color', 'customar_profile': customar_profile, 'pro_active': 'bg-primary text-white'})


class UserProfileUpdate(View):
    def get(self, request):
        user = request.user
        pi = Customer.objects.filter(user=user).exists()
        if pi:
            pi = Customer.objects.get(user=user)
            form = CustomerProfileForm(instance=pi)
        else:
            form = CustomerProfileForm()
        return render(request, 'useraccount/updateprofile.html', {'user_active': 'navbar-active-color', 'form': form, 'up_active': 'bg-primary text-white'})

    def post(self, request):
        user = request.user
        pi = Customer.objects.filter(user=user).exists()
        if pi:
            pi = Customer.objects.get(user=user)
            form = CustomerProfileForm(
                request.POST, request.FILES, instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/profile')
        else:
            form = CustomerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                name = form.cleaned_data['name']
                phone_number = form.cleaned_data['phone_number']
                address = form.cleaned_data['address']
                division = form.cleaned_data['division']
                city = form.cleaned_data['city']
                zip_code = form.cleaned_data['zip_code']
                profile_image = request.FILES['profile_image']
                pro_data = Customer(user=user, name=name, phone_number=phone_number, address=address,
                                    division=division, city=city, zip_code=zip_code, profile_image=profile_image)
                pro_data.save()
                return HttpResponseRedirect('/profile')
        return render(request, 'useraccount/updateprofile.html', {'user_active': 'navbar-active-color', 'form': form, 'up_active': 'bg-primary text-white'})


# class UserProfileUpdate(View):
#     def get(self,request):
#         user = request.user
#         form = CustomerProfileForm()
#         return render(request,'useraccount/updateprofile.html',{'form':form,'up_active':'bg-primary text-white'})

#     def post(self,request):
#         form = CustomerProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             user = request.user
#             name = form.cleaned_data['name']
#             phone_number = form.cleaned_data['phone_number']
#             address = form.cleaned_data['address']
#             division = form.cleaned_data['division']
#             city = form.cleaned_data['city']
#             zip_code = form.cleaned_data['zip_code']
#             profile_image = request.FILES['profile_image']
#             pro_data = Customer(user=user,name=name,phone_number=phone_number,address=address,division=division,city=city,zip_code=zip_code, profile_image=profile_image)
#             pro_data.save()
#             form = CustomerProfileForm()
#             return HttpResponseRedirect('/profile')
#         return render(request,'useraccount/updateprofile.html',{'form':form,'up_active':'bg-primary text-white'})


def userAddress(request):
    add = DeliveryAddress.objects.filter(user=request.user)
    return render(request, 'useraccount/address.html', {'user_active': 'navbar-active-color', 'add': add, 'ad_active': 'bg-primary text-white'})


class AddDeliveryAddress(View):
    def get(self, request):
        user = request.user
        form = DeliveryAddressForm()
        return render(request, 'useraccount/adddeliveryaddress.html', {'user_active': 'navbar-active-color', 'form': form, 'dlyAd_active': 'bg-primary text-white'})

    def post(self, request):
        form = DeliveryAddressForm(request.POST)
        if form.is_valid():
            user = request.user
            home_address = form.cleaned_data['home_address']
            division = form.cleaned_data['division']
            district = form.cleaned_data['district']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            adrs_data = DeliveryAddress(user=user, home_address=home_address,
                                        division=division, district=district, city=city, zip_code=zip_code)
            adrs_data.save()
            return HttpResponseRedirect('/address/')
        return render(request, 'useraccount/adddeliveryaddress.html', {'user_active': 'navbar-active-color', 'form': form, 'dlyAd_active': 'bg-primary text-white'})
