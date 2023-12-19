import os

from sqlalchemy import Column, Integer, MetaData, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

PSQL_HOST = os.getenv("DB_HOST")
PSQL_PORT = os.getenv("DB_PORT")
PSQL_USERNAME = os.getenv("DB_USER")
PSQL_PASSWORD = os.getenv("DB_PASS")
PSQL_DB = os.getenv("DB_BASE")

DATABASE_URL = (
    f"postgresql://{PSQL_USERNAME}:{PSQL_PASSWORD}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DB}"
)

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class UserTable(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))


Base.metadata.create_all(bind=engine)
