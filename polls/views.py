from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import FileResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from .files_services import clear_file, video_downloader


import os


class page(ListView):
    template_name = "ytb.html"
    model = Post


class home(ListView):
    template_name = "ytb.html"
    model = Post


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
        filename = video_downloader(value)
        files = open(f"./media/{filename}", "rb")
        file_response = FileResponse(files)

        return file_response
