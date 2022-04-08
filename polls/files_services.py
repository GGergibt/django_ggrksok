import os
from yt_dlp import YoutubeDL
import instaloader

from django.conf import settings

from .models import insta_profiles, profile

from django.contrib.auth.models import User


def clear_file(files):
    os.remove(f"./media/{files}")


def video_downloader(url: str, query_format: str):
    bestvideo = "best[height<=1080]"
    ydl_opts = {
        "format": query_format,
        "outtmpl": "media/youtube/%(id)s.%(ext)s",
        "noplaylist": True,
        "extract-audio": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_id = info_dict.get("id")
        video_ext = info_dict.get("ext")
    file_response = f"{video_id}.{video_ext}"
    return file_response


def insta_download(account_name: str, folder: str, current_user=None):
    try:
        # insta_acs = "insta_accounts"
        # text = call.message.text
        account_name = account_name.lower().split(" ")[0]

        # L = instaloader.Instaloader(dirname_pattern=f"{folder}/{account_name}")
        # profile = stories_download(account_name, L)
        # print(folder)

        # if "instagram" in folder:
        #     L.download_stories(userids=[profile])
        #     # new_data = insta_profiles.objects.create(name=account_name)
        # else:
        #     L.download_highlights(profile)
        store_account = insta_profiles.objects.get_or_create(name=account_name)
        # new_data = insta_profiles.objects.only("id").get(name=account_name).id
        insta_account_id = insta_profiles.objects.get(name=account_name).id
        if current_user != None:
            insert_info_about_stored_profiles = profile.objects.get(
                name=current_user.id
            ).stored_profiles.add(insta_account_id)
        return "OK"
        #     store_account_into_user = users.objects.create(
        #         name=current_user, stored_profiles=account_name
        #     )
        # new_data.insta_prf.add(account_name)
        # users.stored_profiles.set(insta_profiles.objects.get(account_name))
        # new_data.all()

        # send_files_to_telegram(chat_id, text_name, type_download)
        # insert_account_in_database_if_not_exists(chat_id, text_name, insta_acs)

    except instaloader.exceptions.ProfileNotExistsException:
        return "account does''not exists"


def stories_download(profile: str, L: str):
    L.load_session_from_file(
        "ffvgd2020", "/home/gosha/.config/instaloader/session-ffvgd2021"
    )
    profile = L.check_profile_id(profile)

    return profile


# def stories_download(account_name, )
