"""
marketplace/views.py

Views for marketplace product management.

Current features:
- Merchant product list
- Merchant add product
- Shopper product list
"""

# Django messaging framework for success/error messages
from django.contrib import messages

# Login protection
from django.contrib.auth.decorators import login_required

# Helpers for rendering and redirects
from django.shortcuts import redirect, render

# Local imports
from .forms import ProductForm
from .models import Product


# ============================================================
# Merchant Product List
# ============================================================

@login_required
def merchant_product_list(request):
    """
    Show all products owned by the currently logged-in merchant.
    """

    # Only merchants should access this page
    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    # Get only products belonging to this merchant
    products = Product.objects.filter(merchant=request.user).order_by("-created_at")

    # Simple statistics for the dashboard/table
    total_products = products.count()
    active_products = products.filter(is_active=True).count()
    low_stock_products = products.filter(stock__lt=10).count()

    inventory_value = sum(product.price * product.stock for product in products)

    context = {
        "products": products,
        "total_products": total_products,
        "active_products": active_products,
        "low_stock_products": low_stock_products,
        "inventory_value": inventory_value,
    }

    return render(request, "merchant/products.html", context)


# ============================================================
# Merchant Add Product
# ============================================================

@login_required
def merchant_add_product(request):
    """
    Allow a merchant to create a new product.
    """

    # Block non-merchants
    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    # Handle submitted form
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            # Do not save immediately because we need to attach merchant
            product = form.save(commit=False)
            product.merchant = request.user
            product.save()

            messages.success(request, "Product added successfully.")
            return redirect("merchant_products")

    else:
        # Empty form for first page load
        form = ProductForm()

    return render(request, "merchant/add_product.html", {"form": form})


# ============================================================
# Shopper Product List
# ============================================================

def shopper_product_list(request):
    """
    Show active products to shoppers.
    """

    products = Product.objects.filter(is_active=True).order_by("-created_at")

    return render(request, "shopper/product_list.html", {"products": products})


# ============================================================
# File Metadata
# ============================================================

"""
Author: Sadik Mohamud
Project: InstrWear
File: marketplace/views.py
Purpose: Product views for merchant and shopper flows
Framework: Django
"""