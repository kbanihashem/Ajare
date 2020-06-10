from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Rating, Comment
import pytz


def home(request):
    ctx = {
        'products': Product.objects.all()
    }
    return render(request, 'product/list.html', context=ctx)


def detail(request, product_id):
    product =get_object_or_404(Product, pk=product_id)
    rate = 0
    comments = []
    if Rating.objects.filter(product=product, user=request.user).exists():
        rate = Rating.objects.get(product=product, user=request.user).value
    comments = Comment.objects.filter(product=product).order_by("-date")
    return render(request, 'product/detail.html', context={'product': product, 'rate': rate, 'comments': comments})


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


def comment(request, product_id):
    if request.is_ajax and request.method == "POST" and request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        text = request.POST.get("text", None)
        if text is not None and product is not None and len(text) > 0:
            com = Comment.objects.create(product=product, user=request.user, text=text)
            tehran = pytz.timezone("Asia/Tehran")
            date = tehran.normalize(com.date.astimezone(tehran)).strftime("%B %d, %Y, %-I:%M %p")
            date = date.replace("PM", "p.m.")
            return JsonResponse({"date": date, "text": str(com.text)}, status=200)
    return JsonResponse({"error": 'failed'}, status=400)
