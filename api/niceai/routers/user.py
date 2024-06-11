from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..core.db import get_session
from ..services.user import UserService

user_router = r = APIRouter()


@r.get('')
def users_list(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    service = UserService(session)
    results = service.user_list(skip, limit)
    return results


@r.get('/{user_id}')
def get_user(user_id: str, session: Session = Depends(get_session)):
    service = UserService(session)
    return service.get_user(user_id)
