"""
marketplace/forms.py

Forms for creating and updating marketplace products.
"""

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Product form used inside the merchant dashboard modal.
    """

    class Meta:
        model = Product
        fields = [
            "category",
            "name",
            "description",
            "price",
            "stock",
            "image",
            "is_active",
        ]

        widgets = {
            "category": forms.Select(attrs={"class": "merchant-form-input"}),
            "name": forms.TextInput(
                attrs={
                    "class": "merchant-form-input",
                    "placeholder": "Nike Air Max 90",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "merchant-form-input",
                    "placeholder": "Product description...",
                    "rows": 4,
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "merchant-form-input",
                    "placeholder": "99.99",
                    "step": "0.01",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "merchant-form-input",
                    "placeholder": "50",
                }
            ),
            "image": forms.ClearableFileInput(attrs={"class": "merchant-form-input"}),
            "is_active": forms.Select(
                attrs={"class": "merchant-form-input"},
                choices=[(True, "Active"), (False, "Inactive")],
            ),
        }


# ------------------------------------------------------------
# Author: Sadik Mohamud
# Project: InstrWear
# File: marketplace/forms.py
# Purpose: Product creation form
# ------------------------------------------------------------