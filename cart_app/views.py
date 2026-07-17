from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from products_app.models import Product


def cart(request):
    cart = request.session.get("cart", {})
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        products.append({"product": product, "quantity": quantity, "subtotal": subtotal})
    context = {"products": products, "total": total}
    return render(request, "cart/cart.html", context)


def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    product = get_object_or_404(Product, id=product_id)
    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session["cart"] = cart
    messages.success(request, f'"{product.name}" has been added to your cart.')
    return redirect("cart")

def increase_quantity(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] += 1
    request.session["cart"] = cart
    return redirect("cart")

def decrease_quantity(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] -= 1
        if cart[product_id] <= 0:
            del cart[product_id]
    request.session["cart"] = cart
    return redirect("cart")

def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    product = get_object_or_404(Product, id=product_id)
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
    request.session["cart"] = cart
    messages.warning(request, f'"{product.name}" has been removed from your cart.')
    return redirect("cart")


def clear_cart(request):
    request.session["cart"] = {}
    messages.info(request, "Shopping cart has been cleared.")
    return redirect("cart")