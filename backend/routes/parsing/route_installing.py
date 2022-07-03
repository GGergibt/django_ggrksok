from fastapi import APIRouter, Depends, Header

from databaseLogic.models.installModel import Installation_details

from databaseLogic.queryiesToDB.installQuery import (
    insert_installtion_details_to_db,
    select_data,
    select_most_popular_downloadings_of_profile,
)
from databaseLogic.queryiesToDB.userQuery import get_current_user, get_user_by_token

from .instagram import route_insta_install as insta
from .youtube import route_youtube_install as ytb

router = APIRouter()
router.include_router(insta.router, prefix="/instagram", tags=["instagram"])
router.include_router(ytb.router, prefix="/youtube", tags=["youtube"])


@router.post("/add_info_from_auth_user")
def add_info(
    installation: Installation_details,
    # current_user=Depends(get_current_user),
    token: str | None = Header(),
):
    # print(user_hh)
    user = get_current_user(token)
    print(user)

    installation.owner_id = user[0].user_id
    print(installation)

    result = insert_installtion_details_to_db(installation)
    return result


@router.get("/get_download_count")
def installing_count(file_name: str, category: str, token: str | None = Header()):
    user = get_current_user(token)
    result = select_data(
        owner_id=user[0].user_id, account_name=file_name, category=category
    )
    print(result)
    return result


@router.get("/most_popular")
def popular_download_count(category: str, token: str | None = Header()):
    user_id = get_current_user(token)[0].user_id
    result = select_most_popular_downloadings_of_profile(user_id, category)
    return result
