from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Category, Product)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


class ProductModelAdmin(admin.ModelAdmin):
    pass
