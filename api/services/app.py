from dataclasses import dataclass
from typing import List

from sqlmodel import Session, select, func

from models.app import App


@dataclass
class AppListResults:
    total: int
    list: List[App]


class AppService:
    def __init__(self, session: Session):
        self.session = session

    def create_app(self, app: App):
        self.session.add(app)
        self.session.commit()
        self.session.refresh(app)
        return app

    def app_list(self, skip: int = 0, limit: int = 10) -> AppListResults:
        # 查询总数
        total = self.session.exec(select(func.count(App.id))).first()

        # 查询当前分页的数据
        statement = select(App).offset(skip).limit(limit)
        results = self.session.exec(statement).all()
        return AppListResults(total=total, list=results)

    def get_app(self, app_id: str):
        statement = select(App).where(App.id == app_id)
        results = self.session.exec(statement)
        return results.first()

    def update_app(self, app_id: str, **kwargs):
        app = self.get_app(app_id)
        if not app:
            return None
        for key, value in kwargs.items():
            setattr(app, key, value)
        self.session.add(app)
        self.session.commit()
        self.session.refresh(app)
        return app

    def delete_app(self, app_id: str):
        app = self.get_app(app_id)
        if not app:
            return None
        self.session.delete(app)
        self.session.commit()
        return app_id
