from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms.product import ProductForm


# Create your views here.
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "products/product_list.html",
        {"products": products},
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        "products/product_detail.html",
        {"product": product},
    )


def cart(request):
    return render(request, "products/cart.html")


def about(request):
    return render(request, "products/about.html")


def admin_panel(request):
    products = Product.objects.all()

    return render(
        request,
        "products/admin_panel.html",
        {"products": products},
    )


def create_product(request):

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("admin_panel")

    else:
        form = ProductForm()

    return render(
        request,
        "products/create_product.html",
        {"form": form},
    )


def delete_product(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.delete()
        return redirect("admin_panel")

    return render(
        request,
        "products/delete_product.html",
        {"product": product},
    )
