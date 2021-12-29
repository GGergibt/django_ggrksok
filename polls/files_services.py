import os
from yt_dlp import YoutubeDL

from django.conf import settings


def clear_file(files):
    os.remove(f"./media/{files}")


def video_downloader(url: str):
    bestvideo = "best[height<=1080]"
    ydl_opts = {
        "format": bestvideo,
        "outtmpl": "media/%(id)s.%(ext)s",
        "noplaylist": True,
        "extract-audio": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_id = info_dict.get("id")
        video_ext = info_dict.get("ext")
    file_response = f"{video_id}.{video_ext}"
    return file_response
