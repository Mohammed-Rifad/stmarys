from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('home', views.customer_home, name = 'customer_home'),
    path('cart', views.my_cart, name = 'mycart'),
    path('orders', views.orders, name = 'myorders' )
]
