from django import views
from django.contrib import admin
from django.urls import path
from products_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
]