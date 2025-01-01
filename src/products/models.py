from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(_("Category Name"), max_length=100)
    created_At = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category_name

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(_("Company Name"), max_length=100)
    email = models.EmailField(_("Company Email"), max_length=254, unique=True)
    phone_number = models.CharField(_("Company Phone Number"), max_length=20)
    location = models.CharField(_("Location"), max_length=50, null=True)
    created_At = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")
    
    def __str__(self):
        return self.manufacturer_name



class Product(models.Model):
    product_name = models.CharField(_("Product Name"), max_length=100)
    manufacturer_id = models.ForeignKey(Manufacturer, verbose_name=_("Manufacturer"), on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    inventory = models.IntegerField(_("Inteventory"))
    price = models.FloatField(_("Price"))
    created_At = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.product_name