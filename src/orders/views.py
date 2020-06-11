from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import Wallet
from .functions import change_credit
# Create your views here.

@login_required
def increase_credit(request):
    change_credit(request.user, 10000)
    return redirect('users:profile')
