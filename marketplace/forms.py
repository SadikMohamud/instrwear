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


# ------------------------------------------------------------
# Author: Sadik Mohamud
# Project: InstrWear
# File: marketplace/forms.py
# Purpose: Product creation form
# ------------------------------------------------------------
