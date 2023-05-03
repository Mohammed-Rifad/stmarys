from django.shortcuts import render

# Create your views here.

def customer_home(request):
    return render(request,'customer/home.html')

def my_cart(request):
    return render(request,'customer/cart.html')

def orders(request):
    return render(request,'customer/my_orders.html')

