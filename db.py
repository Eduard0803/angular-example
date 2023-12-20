from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@host_adreess:port_number/db_name"
DATABASE_URL = "postgresql://postgres:364648255@localhost:5433/postgres"

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class UserTable(Base):
    __tablename__ = "users"
    id = Column(String(100), primary_key=True, unique=True, nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
