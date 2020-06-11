from .models import Wallet

def change_credit(user, diff_tomans): 
    # >0 for increase and <0 for decrease
    wallet = Wallet.objects.get(user=user)
    wallet.credit_tomans += diff_tomans
    wallet.save()

def get_credit(user):
    wallet = Wallet.objects.get(user=user)
    return wallet.credit_tomans