from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from db import Session, UserTable
from user_schema import User

# users = []

app = FastAPI(
    title="API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_users():
    with Session() as session:
        users_data = session.query(UserTable).all()
        return users_data


@app.get("/{user_id}")
async def get_user(user_id: str):
    with Session() as session:
        user_data = session.query(UserTable).filter_by(id=user_id).first()
        if user_data is None:
            raise HTTPException(status_code=404, detail="User not found")


@app.post("/")
async def create_user(user_data: User):
    try:
        with Session() as session:
            new_user = UserTable(id=str(uuid4()), **user_data.dict())
            session.add(new_user)
            session.commit()
            return new_user
    except:
        raise HTTPException(
            status_code=400, detail="Error occurred while creating user"
        )


@app.delete("/{user_id}")
async def delete_user(user_id: str):
    try:
        with Session() as session:
            user_data = session.query(UserTable).filter_by(id=user_id).first()
            session.delete(user_data)
            session.commit()
    except:
        raise HTTPException(
            status_code=400, detail="Error occurred while deleting user"
        )


if __name__ == "__main__":
    import subprocess as sub

    sub.call(["uvicorn", "server:app", "--reload", "--host", "0.0.0.0"])
    # sub.call(["uvicorn", "server:app", "--reload"])
