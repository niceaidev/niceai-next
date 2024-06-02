from fastapi import APIRouter, Depends
from sqlmodel import Session

from core.db import get_session
from services.dataset import DatasetService, DatasetListResults

dataset_router = r = APIRouter()


@r.get('')
def datasets_list(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)) -> DatasetListResults:
    service = DatasetService(session)
    results = service.dataset_list(skip, limit)
    return results
