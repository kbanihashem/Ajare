from .models import Wallet

def return_money(order):
    wallet = Wallet.objects.get(user=order.user)
    wallet.credit_tomans += order.value + (order.return_date - order.start_date).days * order.price - order.damage_cost_tomans
    wallet.save()
