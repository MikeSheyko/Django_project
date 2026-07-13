from django.contrib import admin
from django.urls import path
from products_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.product_list, name="product_list"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("about/", views.about, name="about"),
    path("dashboard/", views.admin_panel, name="admin_panel"),
    path("dashboard/create/", views.create_product, name="create_product"),
    path("dashboard/edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("dashboard/delete/<int:product_id>/", views.delete_product, name="delete_product",),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )