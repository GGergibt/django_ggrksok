from fastapi import APIRouter, Depends, HTTPException

from databaseLogic.models.userModel import User_table, Tokens

from databaseLogic.queryiesToDB import (
    userQuery as user_query,
)  # insert_user_to_db, select_all_users, get_user_by_email


# from fastapi import Depends
# from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/create")
def create_user(user: User_table):
    result = user_query.insert_user_to_db(user)
    return result


@router.post("/auth")
def auth(form_data: User_table):
    user = user_query.get_user_by_email(email=form_data.email)[0]
    # print(user)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    if not user_query.validate_password(
        password=form_data.password, hashed_password=user.password
    ):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    return user_query.create_user_token(user_id=user.id)


@router.get("/users/me")
def read_users_me(current_user: User_table = Depends(user_query.get_current_user)):
    return current_user


@router.get("/all")
def return_all_users():
    result = user_query.select_all_users()
    return result
