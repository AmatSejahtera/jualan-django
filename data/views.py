from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {
        'title': 'Halaman Beranda',
    }
    return render(request, 'data/dashboard.html', context)

def products(request):
    context = {
        'title': 'Halaman Product',
    }
    return render(request, 'data/products.html', context)

def customer(request):
    context = {
        'title': 'Halaman Customer',
    }
    return render(request, 'data/customer.html', context)
