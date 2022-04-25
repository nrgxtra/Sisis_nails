from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class SisisNailsUser(AbstractBaseUser, PermissionsMixin):
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


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    name = models.CharField(
        max_length=50,
        blank=True,
    )
    phone_number = models.IntegerField(
        blank=True
    )
    user = models.OneToOneField(
        SisisNailsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from signals import *
