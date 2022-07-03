from fastapi import APIRouter

from .users import route_users
from .parsing import route_installing as install

main_router = APIRouter()
main_router.include_router(route_users.router, prefix="/users", tags=["users"])
main_router.include_router(install.router, prefix="/install", tags=["all_install"])
