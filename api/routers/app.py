from fastapi import APIRouter, Depends
from sqlmodel import Session

from core.db import get_session
from services.app import AppService, AppListResults

app_router = r = APIRouter()


@r.get('')
def apps_list(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)) -> AppListResults:
    service = AppService(session)
    results = service.app_list(skip, limit)
    return results
