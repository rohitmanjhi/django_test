from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'), unique=True, null=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
