"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart import views

app_name='cart'

urlpatterns = [
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
path('cart-view',views.cart_view,name='cart_view'),
path('cart-decrement/<int:i>',views.cart_decrement,name='cart_decrement'),
path('cart-remove/<int:i>',views.cart_remove,name='cart_remove'),
path('place-order',views.placeorder,name='placeorder'),
path('status/<u>',views.payment_status,name='payment_status'),
path('orderview/',views.order_view,name='orderview')

]



