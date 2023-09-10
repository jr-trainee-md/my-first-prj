
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email       = models.CharField(max_length=80, unique=True)
    username    = models.CharField(max_length=45, unique=True)
    date_joined = models.DateTimeField(auto_now_add = True)
    ip          = models.CharField(max_length = 40, default = "0.0.0.0")
    last_login  = models.DateTimeField(auto_now = True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Posts(models.Model):
    usr         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, null = True)
    title       = models.CharField(max_length = 40)
    time_create = models.DateTimeField(auto_now_add = True, db_index = True)
    content     = models.TextField()

    def __str__(self):
        return self.title


