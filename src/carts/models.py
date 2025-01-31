from django.db import models
from users.models import User
from products.models import Product
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Customer"), on_delete=models.CASCADE)
    created_At = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True, auto_now_add=False)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity