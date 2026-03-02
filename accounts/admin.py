from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, MerchantProfile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Show role on the list page
    list_display = ("username", "email", "role", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email")

    # Add role field to the edit form
    fieldsets = UserAdmin.fieldsets + (
        ("Role", {"fields": ("role",)}),
    )

    # Add role field to the create form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Role", {"fields": ("role",)}),
    )

@admin.register(MerchantProfile)
class MerchantProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "business_name",)
    search_fields = ("business_name", "user__username", "user__email")