from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustonUserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(_("Full name"), max_length=100)
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    objects = CustonUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    def _str_(self):
        return self.full_name