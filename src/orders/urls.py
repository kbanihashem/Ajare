from django.urls import path
from django.contrib.auth import views as auth_views

from orders import views

app_name="orders"

urlpatterns = [
    path(r'increase_credit/', views.increase_credit, name="increase_credit"),
    path(r'place_order/<int:product_id>/', views.place_order, name="place_order"),
    path('detail/<int:order_id>/', views.detail, name='detail'),
    path('history/', views.history, name='history'),
]
