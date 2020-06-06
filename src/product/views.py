from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Product, Rating


def home(request):
    ctx = {
        'products': Product.objects.all()
    }
    return render(request, 'product/list.html', context=ctx)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    rate = 0
    if Rating.objects.filter(product=product, user=request.user).exists():
        rate = Rating.objects.get(product=product, user=request.user).value
    return render(request, 'product/detail.html', context={'product': product, 'rate': rate})


def rating(request, product_id):
    if request.is_ajax and request.method == "GET" and request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        value = request.GET.get("value", None)
        if value is not None and product is not None:
            if Rating.objects.filter(product=product, user=request.user).exists():
                r = Rating.objects.get(product=product, user=request.user)
                r.value = value
                r.save()
            else:
                Rating.objects.create(product=product, user=request.user, value=value)
            return JsonResponse({"new": product.get_rating()}, status=200)

    return JsonResponse({}, status=400)

