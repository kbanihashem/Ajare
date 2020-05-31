from django.shortcuts import render, redirect
from product.models import Product

def home(request):
    return render(request, 'product/home.html', context=context)

def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product/detail.html', context={'product': product})
    
