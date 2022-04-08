from .models import profile
from django.contrib.auth.hashers import make_password
import django
from django.contrib.auth import login, authenticate

# from django.contrib.auth.models import User


def registration_user(name, password):
    # password = make_password(not_hash_password)
    # i = users.objects.get_or_create(name=name, password=password)
    django_user = profile.objects.get_or_create(username=name, password=password)
    # login(name, password)


# registration_user(name, password)
