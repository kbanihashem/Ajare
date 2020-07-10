from django.urls import path
from django.contrib.auth import views as auth_views

from product import views

app_name="product"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<int:product_id>', views.detail, name='detail'),
    path('ajax/<int:product_id>', views.rating, name='rating_req'),
    path('com/<int:product_id>', views.comment, name='comment_req'),
    path('search/', views.search, name='search'),
]
