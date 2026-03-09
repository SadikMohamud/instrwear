from django.contrib import admin
from django.urls import path
from core.views import (
    landing,
    choose_role,
    shopper_onboarding,
    merchant_onboarding,
    shopper_dashboard,
    merchant_dashboard,
    shopper_orders,
)
from accounts.views import login_view, logout_view, register_choice, register_shopper, register_merchant

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing, name="landing"),
    path("choose-role/", choose_role, name="choose_role"),

    path("accounts/login/", login_view, name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    path("accounts/register/", register_choice, name="register_choice"),
    path("accounts/register/shopper/", register_shopper, name="register_shopper"),
    path("accounts/register/merchant/", register_merchant, name="register_merchant"),

    path("shopper/dashboard/", shopper_dashboard, name="shopper_dashboard"),
    path("merchant/dashboard/", merchant_dashboard, name="merchant_dashboard"),
    path('shopper/orders/', shopper_orders, name='shopper_orders'),
    path('shopper/onboarding/', shopper_onboarding, name='shopper_onboarding'),
    path('merchant/onboarding/', merchant_onboarding, name='merchant_onboarding'),
]