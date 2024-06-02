from dataclasses import dataclass
from typing import List

from sqlmodel import Session, select, func

from models.provider import Provider


@dataclass
class ProviderListResults:
    total: int
    list: List[Provider]


class ProviderService:
    def __init__(self, session: Session):
        self.session = session

    def create_provider(self, provider: Provider) -> Provider:
        self.session.add(provider)
        self.session.commit()
        self.session.refresh(provider)
        return provider

    def provider_list(self, skip: int = 0, limit: int = 10) -> ProviderListResults:
        # 查询总数
        total = self.session.exec(select(func.count(Provider.id))).first()

        # 查询当前分页的数据
        statement = select(Provider).offset(skip).limit(limit)
        results = self.session.exec(statement).all()
        return ProviderListResults(total=total, list=results)

    def get_provider(self, provider_id: str):
        statement = select(Provider).where(Provider.id == provider_id)
        results = self.session.exec(statement)
        return results.first()

    def update_provider(self, provider_id: str, **kwargs):
        provider = self.get_provider(provider_id)
        if not provider:
            return None
        for key, value in kwargs.items():
            setattr(provider, key, value)
        self.session.add(provider)
        self.session.commit()
        self.session.refresh(provider)
        return provider

    def delete_provider(self, provider_id: str):
        provider = self.get_provider(provider_id)
        if not provider:
            return None
        self.session.delete(provider)
        self.session.commit()
        return provider_id
