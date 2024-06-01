from fastapi import APIRouter, Depends
from sqlmodel import Session

from core.db import get_session
from services.apps import AppService

app_router = r = APIRouter()


@r.get('')
def apps_list(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    service = AppService(session)
    results = service.app_list(skip, limit)
    return results
