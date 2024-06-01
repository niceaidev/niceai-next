from fastapi import APIRouter, Depends
from sqlmodel import Session

from core.db import get_session
from services.provider import ProviderService

provider_router = r = APIRouter()


@r.get('')
def providers_list(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    service = ProviderService(session)
    results = service.provider_list(skip, limit)
    return results


@r.get('/{provider_id}')
def get_provider(provider_id: str, session: Session = Depends(get_session)):
    service = ProviderService(session)
    return service.get_provider(provider_id)
