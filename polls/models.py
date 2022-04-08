from django.db import models

# from django.contrib.auth.base_user import BaseUserManager

# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from django.utils import timezone


class profile(AbstractBaseUser, PermissionsMixin):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    # name = models.ForeignKey(User, on_delete=models.CASCADE)
    stored_profiles = models.ManyToManyField("insta_profiles", blank=True)
    # email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []
    # objects = CustomUserManager()

    def __str__(self):
        return str(self.name)


class insta_profiles(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """

#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_("The Email must be set"))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)

#         # if extra_fields.get("is_staff") is not True:
#         #     raise ValueError(_("Superuser must have is_staff=True."))
#         # if extra_fields.get("is_superuser") is not True:
#         #     raise ValueError(_("Superuser must have is_superuser=True."))
#         # return self.create_user(email, password, **extra_fields)
