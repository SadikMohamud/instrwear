"""
Author: Sadik Mohamud
Project: InstrWear
File: marketplace/views.py
Purpose: Product, cart, and checkout views for merchant and shopper flows
Framework: Django
"""

# ============================================================
# Imports
# ============================================================

import os

import stripe
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import CheckoutForm, ProductForm
from .models import Cart, CartItem, Category, Order, OrderItem, Product

# Configure Stripe using environment variable
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "")


# ============================================================
# Helper Functions
# ============================================================

def _get_or_create_cart(user):
    """
    Ensure the logged-in shopper always has a cart.
    """
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


def _get_cart_count(user):
    """
    Return total quantity of items in the shopper cart.
    """
    if not user.is_authenticated:
        return 0

    if getattr(user, "role", "") != "shopper":
        return 0

    cart = getattr(user, "cart", None)

    if not cart:
        return 0

    return sum(item.quantity for item in cart.items.all())


# ============================================================
# Merchant Product List
# ============================================================

@login_required
def merchant_product_list(request):
    """
    Show all products owned by the currently logged-in merchant.
    """

    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    products = Product.objects.filter(merchant=request.user).order_by("-created_at")

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
    Allow a merchant to create a new product from a dedicated page.
    """

    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.merchant = request.user
            product.save()

            messages.success(request, "Product added successfully.")
            return redirect("merchant_products")
    else:
        form = ProductForm()

    return render(request, "merchant/add_product.html", {"form": form})


# ============================================================
# Shopper Product List
# ============================================================

def shopper_product_list(request):
    """
    Display all active and in-stock products for shoppers.
    Supports search, category filter, sorting, and cart count.
    """

    products = Product.objects.filter(
        is_active=True,
        stock__gt=0,
    ).select_related("merchant", "merchant__merchant_profile", "category")

    categories = Category.objects.all().order_by("name")

    query = (request.GET.get("q") or "").strip()
    if query:
        products = products.filter(name__icontains=query)

    category_slug = (request.GET.get("category") or "").strip()
    if category_slug:
        products = products.filter(category__slug=category_slug)

    sort = (request.GET.get("sort") or "newest").strip()

    if sort == "price_low":
        products = products.order_by("price", "-created_at")
    elif sort == "price_high":
        products = products.order_by("-price", "-created_at")
    else:
        products = products.order_by("-created_at")

    context = {
        "products": products,
        "categories": categories,
        "cart_count": _get_cart_count(request.user),
    }

    return render(request, "shopper/products_list.html", context)


# ============================================================
# Shopper Product Detail
# ============================================================

def shopper_product_detail(request, slug):
    """
    Show a single active product using its slug.
    """

    product = get_object_or_404(
        Product,
        slug=slug,
        is_active=True,
    )

    context = {
        "product": product,
        "cart_count": _get_cart_count(request.user),
    }

    return render(request, "shopper/product_detail.html", context)


# ============================================================
# Cart Views
# ============================================================

@login_required
def cart_view(request):
    """
    Show the logged-in shopper's cart.
    """

    if request.user.role != "shopper":
        messages.error(request, "Only shoppers can access the cart.")
        return redirect("landing")

    cart = _get_or_create_cart(request.user)

    context = {
        "cart": cart,
        "cart_count": _get_cart_count(request.user),
    }

    return render(request, "shopper/cart.html", context)


@login_required
def add_to_cart(request, product_id):
    """
    Add a product to the shopper cart.
    """

    if request.user.role != "shopper":
        messages.error(request, "Only shoppers can add items to cart.")
        return redirect("landing")

    product = get_object_or_404(
        Product,
        id=product_id,
        is_active=True,
        stock__gt=0,
    )

    cart = _get_or_create_cart(request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
    )

    if created:
        cart_item.quantity = 1
        cart_item.save()
        messages.success(request, f"{product.name} added to cart.")
    else:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f"{product.name} quantity updated.")
        else:
            messages.warning(request, "You already have the maximum available stock in your cart.")

    return redirect("cart_view")


@login_required
def update_cart_item(request, item_id):
    """
    Update the quantity of an item in the cart.
    """

    if request.user.role != "shopper":
        messages.error(request, "Only shoppers can update cart items.")
        return redirect("landing")

    if request.method != "POST":
        return redirect("cart_view")

    cart = _get_or_create_cart(request.user)

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart=cart,
    )

    try:
        quantity = int(request.POST.get("quantity", 1))
    except ValueError:
        quantity = 1

    if quantity <= 0:
        item.delete()
        messages.success(request, "Item removed from cart.")
        return redirect("cart_view")

    if quantity > item.product.stock:
        messages.error(request, "Requested quantity exceeds available stock.")
        return redirect("cart_view")

    item.quantity = quantity
    item.save()

    messages.success(request, "Cart updated successfully.")
    return redirect("cart_view")


@login_required
def remove_cart_item(request, item_id):
    """
    Remove a single item from the cart.
    """

    if request.user.role != "shopper":
        messages.error(request, "Only shoppers can remove cart items.")
        return redirect("landing")

    cart = _get_or_create_cart(request.user)

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart=cart,
    )

    item.delete()

    messages.success(request, "Item removed from cart.")
    return redirect("cart_view")


# ============================================================
# Checkout Views
# ============================================================

@login_required
def checkout_view(request):
    """
    Create an order from the cart and send the shopper to Stripe Checkout.
    """

    if request.user.role != "shopper":
        messages.error(request, "Only shoppers can checkout.")
        return redirect("landing")

    cart = _get_or_create_cart(request.user)

    if not cart.items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect("shopper_product_list")

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data["full_name"],
                phone=form.cleaned_data["phone"],
                house=form.cleaned_data["house"],
                street=form.cleaned_data["street"],
                city=form.cleaned_data["city"],
                county=form.cleaned_data["county"],
                postcode=form.cleaned_data["postcode"],
                total_price=cart.total_price(),
            )

            line_items = []

            for item in cart.items.select_related("product", "product__merchant"):
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    merchant=item.product.merchant,
                    product_name=item.product.name,
                    product_price=item.product.price,
                    quantity=item.quantity,
                )

                line_items.append(
                    {
                        "price_data": {
                            "currency": "gbp",
                            "product_data": {
                                "name": item.product.name,
                            },
                            "unit_amount": int(item.product.price * 100),
                        },
                        "quantity": item.quantity,
                    }
                )

            if not stripe.api_key:
                messages.warning(
                    request,
                    "Stripe is not configured yet. Order was created locally, but payment is not active."
                )
                return redirect("shopper_orders")

            checkout_session = stripe.checkout.Session.create(
                mode="payment",
                line_items=line_items,
                success_url=request.build_absolute_uri(reverse("checkout_success")) + "?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=request.build_absolute_uri(reverse("checkout_cancel")),
                metadata={
                    "order_id": str(order.id),
                    "user_id": str(request.user.id),
                },
            )

            order.stripe_checkout_session_id = checkout_session.id
            order.save(update_fields=["stripe_checkout_session_id"])

            return redirect(checkout_session.url, code=303)

    else:
        profile = getattr(request.user, "shopper_profile", None)

        initial = {
            "full_name": f"{request.user.first_name} {request.user.last_name}".strip(),
        }

        if profile:
            initial.update(
                {
                    "phone": profile.phone,
                    "house": profile.house,
                    "street": profile.street,
                    "city": profile.city,
                    "county": profile.county,
                    "postcode": profile.postcode,
                }
            )

        form = CheckoutForm(initial=initial)

    context = {
        "cart": cart,
        "form": form,
        "cart_count": _get_cart_count(request.user),
    }

    return render(request, "shopper/checkout.html", context)


@login_required
def checkout_success(request):
    """
    Shopper returns here after Stripe success redirect.
    """

    return render(
        request,
        "shopper/checkout_success.html",
        {"cart_count": _get_cart_count(request.user)},
    )


@login_required
def checkout_cancel(request):
    """
    Shopper returns here if payment was cancelled.
    """

    messages.info(request, "Payment was cancelled.")
    return redirect("cart_view")


# ============================================================
# Stripe Webhook
# ============================================================

@csrf_exempt
def stripe_webhook(request):
    """
    Handle Stripe webhook events.
    """

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET", "")

    if not webhook_secret:
        return HttpResponse(status=200)

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            webhook_secret,
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        order_id = session.get("metadata", {}).get("order_id")

        if order_id:
            try:
                order = Order.objects.get(id=order_id)
            except Order.DoesNotExist:
                return HttpResponse(status=200)

            if order.payment_status != Order.PaymentStatus.PAID:
                order.payment_status = Order.PaymentStatus.PAID
                order.status = Order.Status.PAID
                order.stripe_payment_intent_id = session.get("payment_intent", "")
                order.save(
                    update_fields=[
                        "payment_status",
                        "status",
                        "stripe_payment_intent_id",
                    ]
                )

                for item in order.items.select_related("product"):
                    product = item.product
                    if product.stock >= item.quantity:
                        product.stock -= item.quantity
                        product.save(update_fields=["stock"])

                CartItem.objects.filter(cart__user=order.user).delete()

    return HttpResponse(status=200)