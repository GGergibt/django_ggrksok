# from .models import profile
from django.contrib.auth.hashers import make_password
import django
from django.contrib.auth import login, authenticate

from .models import user


def registration_user(username, password):
    # password = make_password(not_hash_password)
    i = user.objects.get_or_create(username=username, password=make_password(password))
    # django_user = profile.objects.get_or_create(username=name, password=password)
    # login(username, password)


def show_profiles(current_user):
    i = user.objects.get(username=current_user).stored_profiles.all()

    print(current_user)
    # print(i.iterator())
    # name = list()
    # name = list([str(profile) for profile in i.iterator()])
    # print(name[:])
    # print(i[0 : len(i) - 1])
    return i

    # for profile in i.iterator():
    #     print(profile)
    #     name.append(str(profile))

    # print(name)
    # print(name)


# registration_user(name, password)
