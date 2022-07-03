from sqlmodel import Field, Relationship, SQLModel
from enum import Enum


class Category_enum(str, Enum):
    youtube_audio = "audioYtb"
    youtube_video = "videoYtb"
    instagram_stories = "stories"


class Installation_details(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    folder_name: str = Field()
    destination_folder: str = Field()
    download_count: int | None = Field(index=True)
    owner_id: int | None = Field(foreign_key="user_table.id", index=True)
    category: Category_enum
