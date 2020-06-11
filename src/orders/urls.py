from django.urls import path
from django.contrib.auth import views as auth_views

from orders import views

app_name="orders"

urlpatterns = [
    path(r'increase_credit/', views.increase_credit, name="increase_credit"),
]
