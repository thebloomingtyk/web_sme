from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from phonenumber_field.modelfields import PhoneNumberField


from .managers import CustomUserManager

from django.core.validators import RegexValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], default='0123467808')
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'  # Can log in using email or username
    REQUIRED_FIELDS = ['username', 'phone_number']  # Other required fields when creating a user

    def __str__(self):
        return self.username
        
        # email
        # phone_number
        # password_hash
        # mfa_enabled
        # reset_token
        # reset_token_expiry

