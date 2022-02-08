from django.shortcuts import render,redirect
from .models import ProductDetails,Cart,ProductCategory
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from useraccount.models import Customer,DeliveryAddress
from .models import OrderPlaced
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def productPage(request):
    products = ProductDetails.objects.all()
    category = ProductCategory.objects.all()
    return render(request,'ecoshop/products.html',{'shop_active':'navbar-active-color','products':products,'category':category,'all_active':'bg-primary text-white'})


def product_by_category(request,id):
    pro_cata = ProductDetails.objects.filter(product_category=id)
    category = ProductCategory.objects.all()
    return render(request,'ecoshop/productbycategory.html',{'shop_active':'navbar-active-color','products':pro_cata,'category':category})


def productDetail(request,id):
    product = ProductDetails.objects.get(id=id)
    item_already_in_cart = False
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()   
    return render(request,'ecoshop/productdetail.html',{'shop_active':'navbar-active-color','products':product,'item_already_in_cart':item_already_in_cart})


class AddToCard(View):
    def get(self,request):
        if request.user.is_authenticated:
            user = request.user
            product_id = request.GET.get('product_id')
            product = ProductDetails.objects.get(id=product_id)
            is_exist = Cart.objects.filter(user=user,product=product_id)

            if len(is_exist)>0:
                messages.info(request,'Product Alreday Exist in your Cart')
            else:
                Cart(user=user,product=product).save()
                messages.success(request,'Product Add your Cart Successfully')
            return redirect('/cart')
        else:
            return redirect('/cart')

class CartView(View):
    def get(self,request):
        if request.user.is_authenticated:
            user = request.user
            cartProduct = Cart.objects.filter(user=user)
            amount=0.0
            totalamount = 0.0
            price = 0.0
            shippingcost = 150
            cart_product = [cart_item for cart_item in Cart.objects.all() if cart_item.user == user ]
            if cart_product:
                for p in cart_product:
                    if p.product.discount_price:
                        price = p.product.discount_price
                    else:
                        price = p.product.product_price
                    tempamount = (p.quantity * price)
                    amount += tempamount
            return render(request,'ecoshop/addtocart.html',{'cart_active':'navbar-active-color','carts':cartProduct,'amount':amount,'totalamount':amount+shippingcost,'shippingcost':shippingcost})
        else:
            messages.info(request,'Please login first to view your cart')
            return render(request,'ecoshop/addtocart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.quantity+=1
        cart.save()
        amount=0.0
        shippingcost = 150
        cart_product = [cart_item for cart_item in Cart.objects.all() if cart_item.user == request.user ]
        if cart_product:
            for p in cart_product:
                if p.product.discount_price:
                    price = p.product.discount_price
                else:
                    price = p.product.product_price
                pro_amount = (p.quantity * price)
                amount += pro_amount
                # totalamount = amount+shippingcost
            data={
                    'amount':amount,
                    'totalamount':amount+shippingcost,
                    'quantity':cart.quantity,          
                    }
            return JsonResponse(data)

# minus cart item
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.quantity-=1
        cart.save()
        amount=0.0
        shippingcost = 150
        cart_product = [cart_item for cart_item in Cart.objects.all() if cart_item.user == request.user ]
        if cart_product:
            for p in cart_product:
                if p.product.discount_price:
                    price = p.product.discount_price
                else:
                    price = p.product.product_price
                pro_amount = (p.quantity * price)
                amount += pro_amount
                # totalamount = 
            data={
                    'amount':amount,
                    'totalamount':amount+shippingcost,
                    'quantity':cart.quantity,             
                    }
            return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        cart = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        cart.delete()
        amount=0.0
        # shippingcost = 150
        cart_product = [cart_item for cart_item in Cart.objects.all() if cart_item.user == request.user ]
        for p in cart_product:
            if p.product.discount_price:
                price = p.product.discount_price
            else:
                price = p.product.product_price
            pro_amount = (p.quantity * price)
            amount += pro_amount
        if amount==0:
            shippingcost = 0.0
        else:
            shippingcost = 150
        data={
                'amount':amount,
                'totalamount':amount+shippingcost,
                'shippingcost':shippingcost          
                }
        return JsonResponse(data)


class CheckoutView(View):
    def get(self,request):
        if request.user.is_authenticated:
            user = request.user
            profile = Customer.objects.filter(user=user)
            adrs = DeliveryAddress.objects.filter(user=user)
            cart_item = Cart.objects.filter(user=user)
            amount=0.0
            totalamount = 0.0
            shippingcost = 150
            cart_product = [cart_item for cart_item in Cart.objects.all() if cart_item.user == request.user ]
            if cart_product:
                for p in cart_product:
                    if p.product.discount_price:
                        price = p.product.discount_price
                    else:
                        price = p.product.product_price
                    pro_amount = (p.quantity * price)
                    amount += pro_amount
                totalamount = amount+shippingcost
            return render(request,'ecoshop/checkout.html',{'cart_item':cart_item,'profile':profile,'adrs':adrs,'totalamount':totalamount})
        else:
            return redirect('/account/login/')



class PaymentDone(View):
    def get(self,request):
        user = request.user
        cusproid = request.GET.get('cusproid')
        customer = Customer.objects.get(id=cusproid)
        adrsid = request.GET.get('ardsid')
        address = DeliveryAddress.objects.get(id=adrsid)
        paymet = request.GET.get('cashondelivery')
        cart_items = Cart.objects.filter(user=user)
        for cart_item in cart_items:
            OrderPlaced(user=user,customer=customer,product=cart_item.product,quantity=cart_item.quantity,address=address,payment_method=paymet).save()
            cart_item.delete()
        return redirect('order')



class OrderPage(View):
    def get(self,request):
        user = request.user
        orders = OrderPlaced.objects.filter(user=user)
        return render(request,'ecoshop/orders.html',{'user_active':'navbar-active-color','orders':orders})



