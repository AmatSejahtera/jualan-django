from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
    path('barang/', views.home, name='home-alias'),
    path('barang/products/', views.products, name='products-alias'),
    path('barang/customer/', views.customer, name='customer-alias'),
]