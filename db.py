from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_BASE')}"

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class UserTable(Base):
    __tablename__ = 'users'
    id = Column(String(100), primary_key=True, unique=True, nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
