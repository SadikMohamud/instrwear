"""
marketplace/views.py

Views for marketplace product management and shopper browsing.

Current features:
- Merchant product list
- Merchant add product
- Shopper product list
- Shopper product detail
"""

# Django messaging framework for success/error messages
from django.contrib import messages

# Login protection for private views
from django.contrib.auth.decorators import login_required

# Helpers for rendering pages, redirects, and safe object lookup
from django.shortcuts import get_object_or_404, redirect, render

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
    Also calculates simple dashboard statistics for the product list page.
    """

    # Only merchants should access this page
    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    # Get only products belonging to this merchant
    products = Product.objects.filter(merchant=request.user).order_by("-created_at")

    # Calculate simple inventory statistics
    total_products = products.count()
    active_products = products.filter(is_active=True).count()
    low_stock_products = products.filter(stock__lt=10).count()
    inventory_value = sum(product.price * product.stock for product in products)

    # Send everything to the template
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
    Allow a merchant to create a new product from a dedicated page.
    This is still useful even if you mostly add products from the dashboard modal.
    """

    # Only merchants should access this page
    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    # If the form was submitted, bind POST data and uploaded files
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        # Save product if the form is valid
        if form.is_valid():
            product = form.save(commit=False)

            # Attach the logged-in merchant to the product
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

# ============================================================
# Author: Sadik Mohamud
# Project: InstrWear
# File: marketplace/views.py
# Purpose: Customer-facing merchant shop page view
# ============================================================

def shopper_product_list(request):
    """
    Shopper Product List View

    This view displays all products available for shoppers
    to browse and purchase.

    Only products that meet the following conditions appear:
    - Product is active
    - Product has stock available

    This prevents shoppers from seeing unavailable products.
    """

    # Query database for products that are active AND in stock
    products = Product.objects.filter(
        is_active=True,      # product must be active
        stock__gt=0          # product must have stock available
    ).order_by("-created_at")  # newest products appear first

    # Render the shopper products page
    # NOTE:
    # Your repo template name is "products_list.html"
    return render(
        request,
        "shopper/products_list.html",
        {
            "products": products
        }
    )# ============================================================
# Author: Sadik Mohamud
# Project: InstrWear
# File: marketplace/views.py
# Purpose: Customer-facing merchant shop page view
# ============================================================

def shopper_product_list(request):
    """
    Shopper Product List View

    This view displays all products available for shoppers
    to browse and purchase.

    Only products that meet the following conditions appear:
    - Product is active
    - Product has stock available

    This prevents shoppers from seeing unavailable products.
    """

    # Query database for products that are active AND in stock
    products = Product.objects.filter(
        is_active=True,      # product must be active
        stock__gt=0          # product must have stock available
    ).order_by("-created_at")  # newest products appear first

    # Render the shopper products page
    # NOTE:
    # Your repo template name is "products_list.html"
    return render(
        request,
        "shopper/products_list.html",
        {
            "products": products
        }
    )


# ============================================================
# Shopper Product Detail
# ============================================================

def shopper_product_detail(request, slug):
    """
    Show a single active product using its slug.
    If the product does not exist, Django returns a 404 page.
    """

    # Safely fetch the product by slug, only if it is active
    product = get_object_or_404(
        Product,
        slug=slug,
        is_active=True
    )

    context = {
        "product": product,
    }

    return render(request, "shopper/product_detail.html", context)


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