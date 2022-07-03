from sqlmodel import SQLModel, create_engine

db_name = "ggrksok"

psql_url = f"postgresql:///{db_name}"
engine = create_engine(psql_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
