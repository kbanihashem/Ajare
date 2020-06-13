from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from .models import Wallet
from .functions import change_credit
from product.models import Product, Rating
# Create your views here.

@login_required
def increase_credit(request):
    change_credit(request.user, 10000)
    return redirect('users:profile')

@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    rate = 0
    if Rating.objects.filter(product=product, user=request.user).exists():
        rate = Rating.objects.get(product=product, user=request.user).value
    return render(request, 'orders/place_order.html', context={'product': product, 'rate': rate,})
