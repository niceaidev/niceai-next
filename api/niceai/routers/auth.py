from fastapi import APIRouter

auth_router = r = APIRouter()


@r.get('')
def auth():
    return {"message": "Hello World"}
