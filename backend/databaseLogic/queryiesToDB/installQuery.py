from ..databaseConnect import engine
from ..models.installModel import Installation_details
from sqlmodel import Session, select, func, DDL


def select_data(owner_id: int, account_name: str, category: str):
    print(owner_id, account_name, category)
    with Session(engine) as session:
        result = session.exec(
            DDL(
                f"Select max (download_count) from installation_details where owner_id = {owner_id} and folder_name='{account_name}' and category='{category}'"
            )
        )
        return result.scalar()


def insert_installtion_details_to_db(install_data: Installation_details):
    prev_count_for_user = select_data(
        install_data.owner_id, install_data.folder_name, install_data.category
    )
    install_data.download_count = prev_count_for_user + 1 if prev_count_for_user else 1
    with Session(engine) as session:
        session.add(install_data)
        session.commit()
        session.refresh(install_data)
        return install_data


def select_most_popular_downloadings_of_profile(user_id: int, category: str):
    with Session(engine) as session:
        result = session.exec(
            DDL(
                f"SELECT folder_name, MAX(download_count) FROM installation_details WHERE owner_id={user_id} and category='{category}'  GROUP BY folder_name ORDER BY MAX(download_count) DESC"
            )
        )
    return result.all()
