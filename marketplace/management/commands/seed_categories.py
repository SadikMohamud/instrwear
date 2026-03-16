"""
Author: Sadik Mohamud
Project: InstrWear
File: marketplace/management/commands/seed_categories.py
Purpose: Seed default marketplace product categories
Framework: Django
"""

from django.core.management.base import BaseCommand

from marketplace.models import Category


class Command(BaseCommand):
    help = "Seed default product categories for InstrWear"

    def handle(self, *args, **options):
        categories = [
            "T-Shirts",
            "Jeans",
            "Dresses",
            "Shoes",
            "Accessories",
            "Outerwear",
        ]

        for name in categories:
            category, created = Category.objects.get_or_create(name=name)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created category: {category.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Already exists: {category.name}")
                )

        self.stdout.write(self.style.SUCCESS("Category seeding complete."))