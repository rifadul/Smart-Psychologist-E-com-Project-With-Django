from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import Customer,DeliveryAddress



class UserSingupForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class': 'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['email', 'username']
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'current-password','class': 'form-control'})
        }


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )


class MyPasswordchangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),
    )


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','class': 'form-control'})
    )


class MysetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control'})
)


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone_number','address','division','city','zip_code','profile_image']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'division' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'zip_code' : forms.TextInput(attrs={'class':'form-control'}),
            
        }


class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        fields = ['home_address','division','district','city','zip_code']
        widgets = {
            'home_address':forms.TextInput(attrs={'class':'form-control'}),
            'division' : forms.TextInput(attrs={'class':'form-control'}),
            'district' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'zip_code' : forms.TextInput(attrs={'class':'form-control'}),
        }