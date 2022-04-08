from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from .files_services import clear_file, video_downloader, insta_download
from .users_services import registration_user
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
import django
from .models import profile


import os


class page(ListView):
    template_name = "ytb.html"
    # model = Post


class home(ListView):
    template_name = "ytb.html"
def home_page(request):
    return render(request, "ytb.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        # print(not_hash_password)
        # password = make_password(not_hash_password)
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user=user)
            return redirect("admin/")
        # user = users.objects.get(name=username, password=password)
    return render(request, "login.html")
def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        registration_user(username, password)
        user = authenticate(request, username=username, password=password)
        login(request, user=user)
        return redirect("admin/")

        # print(request.user)
    return render(request, "registration.html")

def form_post(request):
    result = os.listdir("./media")
    return render(
        request, "checkbox.html", context={"request": request, "result": result}
    )


@csrf_exempt
def get_file(request):
    my_dict = request.GET.dict()
    for key, value in my_dict.items():
        if "clear" in key:
            clear_file(value)
            result = os.listdir("./media")
            return redirect("/checkbox/")
        else:
            path = f"media/{value}"
            files = open(path, "rb")
            file_response = HttpResponse(files, content_type="video/mp4")

        return file_response


@csrf_exempt
def app_download(request):
    get_dict = request.GET.items()
    for key, value in get_dict:
        print(key)
        match key:
            case "instagram":
                if request.user.is_authenticated:
                    current_user = request.user
                    info_about_result = insta_download(value, "instagram", current_user)
                    if "OK" in info_about_result:
                        
                        return HttpResponse('OK')

            case "url":
                print("goodby")

    #     print(key)
    #     print(value)
    # filename = video_downloader(value, key)
    # # files = open(f"./media/{filename}", "rb")
    # # file_response = FileResponse(files)

    # return HttpResponse('hello')
    # return HttpResponse(file_response)
