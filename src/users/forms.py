from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('full_name', 'email', 'phone_number')
        error_class = 'error'


class ChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('full_name', 'email', 'phone_number', 'is_active', 'is_staff')
        error_class = 'error'