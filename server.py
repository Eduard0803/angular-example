import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse

from db_methods import create_user, get_user, get_users
from user_schema import User

users = []

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
    # get_users()
    users_data = {}
    users_data["users"] = users
    return users_data


@app.get("/user/{email}")
async def get_user(email: str) -> dict:
    # get_user(email)
    for user in users:
        if user.email == email:
            return json.dump(user, indent=4)
    return HTTPException(status_code=404, detail="User not found")


@app.post("/")
async def create_user(user: User) -> None:
    # create_user(user)
    users.append(user)
    return user.dict()


@app.patch("/backup")
async def backup_users_data() -> None:
    users_data = {}
    users_data["users"] = []
    for user in users:
        users_data["users"].append(user.dict())
    with open("users_data.json", "w") as file:
        json.dump(users_data, file, indent=4)


if __name__ == "__main__":
    import subprocess as sub

    sub.call(["uvicorn", "server:app", "--reload", "--host", "0.0.0.0"])
    # sub.call(["uvicorn", "server:app", "--reload"])
