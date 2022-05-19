from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from sisys.sisis_auth.managers import SisisUserManager


class SisisUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.TimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'email'
    manager = SisisUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    phone_number = models.IntegerField(
        blank=True,
        null=True,
    )
    user = models.OneToOneField(
        SisisUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    address = models.TextField()


from .signals import *
