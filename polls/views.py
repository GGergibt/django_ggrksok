from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from .files_services import clear_file, video_downloader, insta_download
from .users_services import registration_user, show_profiles
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.views import View
import django
from django.views.generic.edit import CreateView


from .models import user


import os

# class page(ListView):
#     template_name = "ytb.html"
#     model = Post


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
            return redirect("/")
        # user = users.objects.get(name=username, password=password)
    return render(request, "login.html")
# def registration(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         registration_user(username, password)
#         user = authenticate(request, username=username, password=password)
#         login(request, user=user)
#         return redirect("/")

        # print(request.user)
    # return render(request, "registration.html")
class registration(View):
    def get(self, request):
        return render(request, "registration.html")
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        # user.custom_objects.registration_user(username, password)
        registration_user(username, password)
        auth_user = authenticate(request, username=username, password=password)
        login(request, user=auth_user)
        return redirect("/")

def form_post(request):
    stored_profile = request.GET.get("folder")
    print(stored_profile)
    if stored_profile == None:
        stored_profile = "youtube"
        result = os.listdir(f"media/{stored_profile}")
    # elif stored_profile == "youtube":
        # result = os.listdir(f"media/{stored_profile}")
    else:


    # folder = os.listdir(f"media/{stored_profile}")
        folder = os.listdir(f"media/{stored_profile}")
    # result = filter(filter_directory, folder)
        result = sorted(delete_dublicates(folder))

    # print(result)
    return render(
            request, "checkbox.html", context={"request": request, "result": result, "stored_profile": stored_profile}
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
            path = f"media/{key}/{value}"
            files = open(path, "rb")
            # print(files)
            if ".mp4" in value:
                file_response = HttpResponse(files, content_type="video/mp4")

                return file_response
            elif ".jpg" in value:
                file_response = HttpResponse(files, content_type="image/jpg")
                return file_response

            else:
                file_response = HttpResponse(files)
                return file_response

def filter_directory(folder_file):
    if ".json" in folder_file:
        return False
    else:
        return True
def delete_dublicates(folder_file):
    # print(folder_file)
    jpg_list = [i.split(".")[0] for i in folder_file if ".jpg" in i]
    video_list = [r.split(".")[0] for r in folder_file if ".mp4" in r]
    # print(jpg_list)
    # print(video_list)
    count = 0
    while count < len(video_list):
        print(count)
        if video_list[count] in jpg_list:
            jpg_list.remove(video_list[count])
            count +=1
        # pass
    new_jpg_list = [i+".jpg" for i in jpg_list ]
    new_video_list = [i+".mp4" for i in video_list]
    return new_video_list + new_jpg_list
    # if video_list[count] in jpg_list:
        # print(video_list[count])
        # print(jpg_list)





def return_stored_profiles(request):
    if request.user.is_authenticated:
        current_user = request.user
        stored_profiles = show_profiles(current_user)
        return render(request,"show_profiles.html", {'stored_profiles': stored_profiles} )
    return render(request, "show_profiles.html")

@csrf_exempt
def app_download(request):
    get_dict = request.GET.items()
    for key, value in get_dict:
        print(key)
        match key:
            case "instagram":
                if request.user.is_authenticated:
                    current_user = request.user
                    info_about_result = insta_download(value, "media/", current_user)
                    if "OK" in info_about_result:

                        return redirect("/") 

            case "url":
                print("goodby")
                video_downloader(value, "best")
                return redirect("/") 

# class test_view(CreateView):
#     success_url = '/'
#     model = user

#     fields = ['username', 'password']



    #     print(key)
    #     print(value)
    # filename = video_downloader(value, key)
    # # files = open(f"./media/{filename}", "rb")
    # # file_response = FileResponse(files)

    # return HttpResponse('hello')
    # return HttpResponse(file_response)
