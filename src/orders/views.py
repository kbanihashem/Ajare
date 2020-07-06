import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.contrib import messages


from .models import Wallet, Order
from .functions import change_credit, get_credit
from product.models import Product, Rating
from .forms import OrderCreateForm
# Create your views here.
@login_required
def history(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'orders/history.html', context={'orders': orders})

@login_required
def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.user != request.user:
        return HttpResponseNotFound('Not your order pal. Now fuck off')

    return render(request, 'orders/detail.html', context={'order': order})

@login_required
def increase_credit(request):
    change_credit(request.user, 10000)
    return redirect('users:profile')

@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data.get('duration')
            to_pay = product.price * duration + product.value
            user = request.user
            if to_pay <= get_credit(user):
                change_credit(user, -to_pay)
                order = Order.objects.create(
                        user=request.user,
                        start_date=form.cleaned_data.get('start_date'),
                        duration=duration,
                        product=product,
                        value=product.value,
                        price=product.price,
                        status=Order.STATUS_PAID,
                        )
                messages.success(request, f"Order for {product.name} estblished")
                return redirect("orders:detail", order_id=order.pk)
            else:
                form.add_error(None, 'Note enough money')
        else:
            pass

    else:
        form = OrderCreateForm({
            'start_date': datetime.date.today(),
            'duration': 7,
            })

    rate = 0
    if Rating.objects.filter(product=product, user=request.user).exists():
        rate = Rating.objects.get(product=product, user=request.user).value
    context = {
            'form': form,
            'product': product,
            'rate': rate,
            }
    return render(request, 'orders/place_order.html', context=context)
