from fastapi import FastAPI

from databaseLogic.databaseConnect import create_db_and_tables
from routes import mainRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:3000",
    "http://127.0.0.1:8000/",
]


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.mount("/media/youtube", StaticFiles(directory="media/youtube"), name="media")
app.mount("/media/instagram", StaticFiles(directory="media/instagram"), name="media")


app.include_router(mainRouter.main_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.post("/")
# def create_user(user: User):
#     result = insert_user_to_db(user)
#     return result
