from django.urls import path
from django.contrib.auth import views as auth_views

from product import views

app_name="product"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<int:product_id>', views.detail, name='detail'),
]
