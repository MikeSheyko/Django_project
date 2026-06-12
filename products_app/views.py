from django.shortcuts import render
from django.http import Http404

products = [
    {
        'id': 1,
        'name': 'iPhone X',
        'description': 'Description for product 1',
        'price': 19.99,
        'stock': 10,
        'category': 'electronics',
        'discount': 10,
        'image': 'https://content1.rozetka.com.ua/goods/images/big/221203654.jpg',
    },
    {
        'id': 2,
        'name': 'Samsung Galaxy S21',
        'description': 'Description for product 2',
        'price': 29.99,
        'stock': 5,
        'category': 'clothing',
        'discount': 20,
        'image': 'https://content.rozetka.com.ua/goods/images/big/487792065.jpg',
    },
    {
        'id': 3,
        'name': 'MacBook Pro',
        'description': 'Description for product 3',
        'price': 9.99,
        'stock': 20,
        'category': 'books',
        'discount': 0,
        'image': 'https://content1.rozetka.com.ua/goods/images/big_tile/655338574.jpg',
    },
]

# Create your views here.
def product_list(request):
    # additional logic (get data from db, validate forms, etc.) can be added here
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = next((item for item in products if item["id"] == product_id), None)

    if product is None:
        raise Http404("Product not found")

    return render(request, "products/product_detail.html", {"product": product})

def about(request):
    return render(request, 'products/about.html')
