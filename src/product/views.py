from django.shortcuts import render, redirect
from product.models import Product

def home(request):
    ctx = {
        'products': Product.objects.all()
    }
    return render(request, 'product/list.html', context=ctx)

def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product/detail.html', context={'product': product})
    
