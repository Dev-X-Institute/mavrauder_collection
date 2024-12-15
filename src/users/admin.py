from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import RegistrationForm, ChangeForm
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = RegistrationForm
    form = ChangeForm
    model = User
    list_display = ['full_name', 'email', 'phone_number','is_active', 'is_staff']
    list_display_links = ['email']
    search_fields = ['email', 'full_name', 'phone_number']
    list_filter = ['full_name', 'email', 'phone_number','is_active', 'is_staff']
    fieldsets = (
        (
            _("Login Credentials"), {
                "fields": ("email", "password",)
            }, 
        ),
        (
            _("Personal Information"),
            {
                "fields": ('full_name', 'phone_number',)
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": ("last_login",)
            },
        ),
    )
    add_fieldsets = (
            (None, {
                "classes": ("wide",),
                "fields": ("email", "full_name", "phone_number", "password1", "password2", "is_staff", "is_active"),
            },),
        )


admin.site.register(User, UserAdmin)