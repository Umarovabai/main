from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string

MSG = 'Нужно указать email'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra):
        if not email:
            msg = (MSG)
            raise ValueError(msg)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra):
        if not email:
            raise ValueError(MSG)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        print(user)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=25, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_activation_code(self):
        code = get_random_string(length=25, allowed_chars='!@#$%^&*()1234567890qwertyuiop')
        self.activation_code = code

        def __str__(self):
            return self.email






















