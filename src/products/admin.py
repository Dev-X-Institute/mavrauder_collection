from django.contrib import admin
from .models import Category, Manufacturer, Product

# Register your models here.
admin.site.register([Category, Manufacturer, Product])