from django.contrib import admin
from django.urls import path
# ----------- import for media file ----------------- #
from django.conf import settings
from django.conf.urls.static import static
# ----------- import for Login,Logout authentication and render template ----------------- #
from django.contrib.auth import views as auth_views
# ----------- import core views ----------------- #
from core import views as cor_views
# ----------- import blog Apps views ----------------- #
from blog import views as blog_views
# ----------- import useraccount Apps views ----------------- #
from useraccount import views as user_views
# ----------- import doctor Apps views ----------------- #
from doctor import views as doc_views
# ----------- import eshop Apps views ----------------- #
from ecoshop import views as eco_views
# ----------- import form.py file from useraccount App  ----------------- #
from useraccount.form import UserLoginForm,MyPasswordchangeForm,MyPasswordResetForm,MysetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    # ----------- set url for core Apps ----------------- #
    path('',cor_views.home, name='home'),

# ----------- set url for blog Apps ----------------- #
    path('blog/',blog_views.blog, name='blog'),
    path('blogdetails/<slug>',blog_views.blogDetails, name='blogDetails'), 

# ----------- set url for useraccount Apps ----------------- #
    path('account/registration/',user_views.UserRegistration.as_view(),name='registration'),
    path('account/login/',auth_views.LoginView.as_view(template_name='useraccount/userlogin.html',authentication_form=UserLoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='useraccount/passwordchange.html',form_class=MyPasswordchangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='useraccount/passwordchangedone.html'),name='passwordchangedone'),
    path('profile/',user_views.UserProfile.as_view(),name='profile'), 
    path('updateprofile/',user_views.UserProfileUpdate.as_view(),name='updateprofile'), 

    # path('profileup/<int:pk>/',user_views.profiletest,name='profileup'), 
    # path('profileup/',user_views.profiletest,name='profileup'), 


    path('address/',user_views.userAddress,name='address'),
    path('deliveryaddress/',user_views.AddDeliveryAddress.as_view(),name='deliveryaddress'), 
# ----------- for password reset url ----------------- #

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='useraccount/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='useraccount/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='useraccount/password_reset_confirm.html',form_class=MysetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='useraccount/password_reset_complete.html'),name='password_reset_complete'),


# ----------- import doctor Apps views ----------------- #
    path('doctor/',doc_views.doctorInfo,name='doctor'),
    path('doctordetails/<int:id>/',doc_views.doctorDetails, name='doctorDetails'),

# ----------- set url for eshop Apps ----------------- #
    path('shop/', eco_views.productPage, name='shop'),
    path('productdetail/<int:id>/', eco_views.productDetail, name='productdetail'),
    path('productbycategory/<int:id>/', eco_views.product_by_category, name='productbycategory'),
    path('add-to-cart/', eco_views.AddToCard.as_view(), name='add-to-cart'),
    path('cart/',eco_views.CartView.as_view(), name='cart'),
    path('pluscart/',eco_views.plus_cart),
    path('minuscart/',eco_views.minus_cart),
    path('removecart/',eco_views.remove_cart),
    path('checkout/',eco_views.CheckoutView.as_view(), name='checkout'),
        path('orders/',eco_views.OrderPage.as_view(),name='orders'),
    path('paymentdone/',eco_views.PaymentDone.as_view(), name='paymentdone'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
