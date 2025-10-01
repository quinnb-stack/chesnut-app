import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dotenv_path = Path("env/.env")
load_dotenv(dotenv_path=dotenv_path)

MYSQL_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")

database_names = [
    "herbal_db",
    "smes_db",
]

databases = {}
for db_name in database_names:
    db_connect = f"mysql+mysqlconnector://root:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{db_name}"
    engine = create_engine(db_connect, pool_pre_ping=True)
    databases[db_name] = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db(database_name: str):
    db = databases[database_name]()
    try:
        yield db
    finally:
        db.close()


class DatabaseSessionMaker:
    """
    Creates a new session to be used for database operations.

    See Referring to a new database section in README.md
    """

    def __init__(self, database_name: str):
        self.database_name = database_name

    def __call__(self):
        if self.database_name not in database_names:
            raise KeyError("Database name invalid")

        db = databases[self.database_name]()
        try:
            yield db
        finally:
            db.close()
