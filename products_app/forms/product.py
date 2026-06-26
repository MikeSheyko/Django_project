from django import forms
from products_app.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ["name", "image", "description", "price", "stock", "category", "discount",]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Product name"
            }),
            "image": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Image URL"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Description"
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01"
            }),
            "stock": forms.NumberInput(attrs={
                "class": "form-control"
            }),
            "category": forms.Select(attrs={
                "class": "form-select"
            }),
            "discount": forms.NumberInput(attrs={
                "class": "form-control"
            }),
        }