"""
Author: Sadik Mohamud
Project: InstrWear
File: marketplace/forms.py
Purpose: Forms for merchant product creation and shopper checkout
Framework: Django
"""

from django import forms

from .models import Product


# ============================================================
# Merchant Product Form
# ============================================================

class ProductForm(forms.ModelForm):
    """
    Form used by merchants to create and manage products.
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
            "category": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Product name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Product description",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                }
            ),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def clean_price(self):
        """
        Ensure price cannot be negative.
        """
        price = self.cleaned_data["price"]
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

    def clean_stock(self):
        """
        Ensure stock cannot be negative.
        """
        stock = self.cleaned_data["stock"]
        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock


# ============================================================
# Shopper Checkout Form
# ============================================================

class CheckoutForm(forms.Form):
    """
    Form used by shoppers during checkout.

    Captures delivery details before Stripe Checkout starts.
    """

    full_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Full name",
            }
        ),
    )

    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Phone number",
            }
        ),
    )

    house = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "House / Flat number",
            }
        ),
    )

    street = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Street",
            }
        ),
    )

    city = forms.CharField(
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "City",
            }
        ),
    )

    county = forms.CharField(
        max_length=120,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "County",
            }
        ),
    )

    postcode = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Postcode",
            }
        ),
    )