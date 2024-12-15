from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustonUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("A valid email must be provided"))
        
    def create_user(self, full_name, email, password, **extra_fields):

        if not full_name:
            raise ValueError(_("Users must provided a name"))
        
        if email:
            email = self.normalize_email(email=email)
            self.email_validator(email=email)
        else:
            raise ValueError(_("An email address is required"))
        
        user = self.model(
            full_name=full_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save()
        
        return user
    

    def create_superuser(self, full_name, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_active=True"))
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must be is_superuser=True"))
        
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superusers must be is_active=True"))
        
        if not password:
            raise ValueError(_("Superuser must have a password"))
        
        if email:
            email = self.normalize_email(email=email)
            self.email_validator(email=email)
        else:
            raise ValueError(_("Admin User: An email address is required"))
        
        user = self.create_user(full_name=full_name, email=email, password=password, **extra_fields)
        user.save()

        return user