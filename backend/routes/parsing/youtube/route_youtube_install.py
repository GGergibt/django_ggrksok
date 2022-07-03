from yt_dlp import YoutubeDL

import sys

from fastapi import APIRouter


router = APIRouter()

@router.post("/video")
def video_downloader(url: str, query_format: str):
    bestvideo = "best[height<=1080]"
    print(query_format)
    match query_format:
        case "best":
            category = "videoYtb"
        case "bestaudio":
            category = "audioYtb"
    ydl_opts = {
        "format": query_format,
        # "outtmpl": "/home/gosha/projects/react_ggrksok/frontend/public/youtube/%(id)s.%(ext)s",
        "outtmpl": "/home/gosha/projects/react_ggrksok/backend/media/youtube/%(id)s.%(ext)s",
        "noplaylist": True,
        "extract-audio": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_id = info_dict.get("id")
        video_ext = info_dict.get("ext")
    # file_response = f"/home/gosha/projects/react_ggrksok/frontend/public/youtube/{video_id}.{video_ext}"
    file_response = f"/home/gosha/projects/react_ggrksok/backend/media/youtube/{video_id}.{video_ext}"
    return {
        "destination_folder": file_response,
        "folder_name": f"{video_id}.{video_ext}",
        "category": category,
    }
