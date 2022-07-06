import instaloader

from os import listdir
from fastapi import APIRouter

router = APIRouter()


@router.post("/install_stories/{account_name}")
def install(account_name: str):
    destination_folder = (
        f"/home/gosha/projects/react_ggrksok/backend/media/instagram/{account_name}"
    )
    try:
        L = instaloader.Instaloader(dirname_pattern=destination_folder)
        # auth_user = "ffvgd2021"
        profile = login_account(account_name, L)

        # if "instagram" in type_download:
        # user_posts = [L.download_post(i, account_name) for i in user.get_posts()]
        # for user_post in account_name.get_posts():
        #     # while max_count_likes_profile < 1:
        #     print("hello")
        #     L.download_post(user_post, account_name)
        L.download_stories(userids=[profile])
        # else:
        #     L.download_highlights(profile)

        return {
            "destination_folder": destination_folder,
            "folder_name": account_name,
            "category": "stories",
        }

        # send_files_to_telegram(chat_id, text_name, type_download)
        # insert_account_in_database_if_not_exists(chat_id, text_name, insta_acs)
        # stored_profiles_for_user_in_db(chat_id, text_name, insta_acs)

    except instaloader.exceptions.ProfileNotExistsException:
        pass


@router.get("/get/{account_name}")
def returning(account_name: str):
    destination_folder = (
        f"/home/gosha/projects/react_ggrksok/backend/media/instagram/{account_name}"
    )
    files = listdir(destination_folder)
    print(files)
    return {"files": files}


def login_account(profile: str, L: str):
    L.load_session_from_file(
        "ffvgd2021", f"/home/gosha/.config/instaloader/session-ffvgd2021"
    )
    profile = L.check_profile_id(profile)

    return profile
