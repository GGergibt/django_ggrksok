from ..databaseConnect import engine
from ..models.userModel import User_table, Tokens
from sqlmodel import Session, DDL
import hashlib
import random
import string
from datetime import datetime, timedelta, date
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/auth")


def select_all_users():
    with Session(engine) as session:
        result = session.exec(DDL("SELECT * FROM user_table")).all()
        return result


def insert_user_to_db(user_data: User_table):
    salt = get_random_string()
    hashed_password = hash_password(user_data.password, salt)
    # query = user.insert().values(
    #     email=user.email, name=user.name, hashed_password=f"{salt}${hashed_password}"
    # )
    user_data.password = f"{salt}${hashed_password}"
    with Session(engine) as session:
        user_id = session.exec(
            DDL(
                f"insert into user_table (email, name, password) values('{user_data.email}', '{user_data.name}', '{salt}${hashed_password}') Returning id;"
            )
        ).scalar()
        # print(user_id)

        # session.add(
        #     user_data
        #     # email=user_data.email,
        #     # password=f"{salt}${hashed_password}",
        # )
        session.commit()
        # session.refresh(user_data)
        # user_id = session.exec(
        #     f"select id from user_table where email= '{user_data.email}'"
        # ).scalar()

        token = create_user_token(user_id)
        token_dict = {"token": token.token, "expires": token.expires}
        return {
            **user_data.dict(),
            "id": user_id,
            "is_active": True,
            "token": token_dict,
        }


# async def create_user(user: user_schema.UserCreate):
#     """Создает нового пользователя в БД"""
#     user_id = await database.execute(query)
#     token = await create_user_token(user_id)
#     token_dict = {"token": token["token"], "expires": token["expires"]}

#     return {**user.dict(), "id": user_id, "is_active": True, "token": token_dict}
# def get_current_user(token: str = Depends(oauth2_scheme)):
def get_current_user(token: str):
    print(token)
    user = get_user_by_token(token)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # if not user.is_active:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
    #     )
    return user


def get_random_string(length=12):
    """Генерирует случайную строку, использующуюся как соль"""
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def hash_password(password: str, salt: str = None):
    """Хеширует пароль с солью"""
    if salt is None:
        salt = get_random_string()
    enc = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return enc.hex()


def validate_password(password: str, hashed_password: str):
    """Проверяет, что хеш пароля совпадает с хешем из БД"""
    salt, hashed = hashed_password.split("$")
    return hash_password(password, salt) == hashed


def get_user_by_token(token: str):
    with Session(engine) as session:
        print(date.today())
        # query = DDL(
        #     f"SELECT * FROM user_table JOIN tokens ON user_table.id = tokens.user_id where token='{token}'"
        # )
        query = DDL(
            f"SELECT * FROM user_table JOIN tokens ON user_table.id = tokens.user_id where token='{token}' and expires > '{date.today()}'"
        )
        return session.exec(query).all()


def get_user_by_email(email: str):
    """Возвращает информацию о пользователе"""
    with Session(engine) as session:
        query = DDL(f"SELECT * FROM user_table WHERE email = '{email}'")
        # query = users.select().where(users.email == email)
        return session.exec(query).all()


# async def get_user_by_token(token: str):
#     """Возвращает информацию о владельце указанного токена"""
#     query = (
#         tokens_table.join(users_table)
#         .select()
#         .where(
#             and_(tokens_table.c.token == token, tokens_table.c.expires > datetime.now())
#         )
#     )
#     return await database.fetch_one(query)


def create_user_token(user_id):

    """Создает токен для пользователя с указанным user_id"""
    token = Tokens()

    with Session(engine) as session:
        date_expires = date.today() + timedelta(weeks=2)
        token.expires = date_expires
        token.user_id = user_id
        select_tokens_details = DDL(
            f"SELECT token, expires FROM tokens WHERE user_id={user_id} and expires = '{date_expires}'"
        )
        result = session.exec(select_tokens_details).all()
        print(result)
        if result:
            return result[0]
        session.add(token)
        # query = DDL(
        #     f"INSERT INTO tokens (expires, user_id) VALUES('{date_expires}', {user_id}) returning token, expires;"
        # )
        session.commit()
        session.refresh(token)
        result = session.exec(select_tokens_details).all()
        return result[0]

        # query = (
        #     Tokens.insert()
        #     .values(expires=datetime.now() + timedelta(weeks=2), user_id=user_id)
        #     .returning(Tokens.token, Tokens.expires)
        # print(result[0].expires)
        # for column, value in result[0].items():

        #     print(column, value)
        # print(result)
        print(result)
        # )
