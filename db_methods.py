from db import Session, UserTable
from user_schema import User


def create_user(user: User) -> None:
    with Session() as session:
        new_user = UserTable(**user.dict())
        session.add(new_user)
        session.commit()


def get_user(email: str):
    with Session() as session:
        user = session.query(UserTable).filter_by(email=email).first()
        if user:
            return user
        return None


def get_users():
    with Session() as session:
        users = session.query(UserTable).all()
        return users
