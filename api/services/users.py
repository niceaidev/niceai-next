from sqlmodel import Session, select, func
from typing import List, Optional
from dataclasses import dataclass

from models.user import User


@dataclass
class UserListResults:
    total: int
    list: List[User]


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def user_list(self, skip: int = 0, limit: int = 10) -> UserListResults:
        # 查询总数
        total = self.session.exec(select(func.count(User.id))).first()

        # 查询当前分页的数据
        statement = select(User).offset(skip).limit(limit)
        results = self.session.exec(statement).all()
        return UserListResults(total=total, list=results)

    def get_user(self, user_id: str):
        print(user_id)
        statement = select(User).where(User.id == user_id)
        results = self.session.exec(statement)
        return results.first()

    def update_user(self, user_id: str, **kwargs):
        user = self.get_user(user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            setattr(user, key, value)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete_user(self, user_id: str):
        user = self.get_user(user_id)
        if not user:
            return None
        self.session.delete(user)
        self.session.commit()
        return user_id
