from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.crypto import get_random_string

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """Creates and saves a User with the given email, username, and password."""
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """Creates and saves a superuser with the given email, username, and password."""
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
def generate_random_password():
    return get_random_string(12)  # 12 character random password

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200, default=generate_random_password)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # The field used to log in
    REQUIRED_FIELDS = ['username']  # Additional required fields

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app?"""
        return True
