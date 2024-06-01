from sqlmodel import Session, select, func
from typing import List, Optional
from dataclasses import dataclass
from models.dataset import Dataset


@dataclass
class DatasetListResults:
    total: int
    list: List[Dataset]


class DatasetService:
    def __init__(self, session: Session):
        self.session = session

    def create_dataset(self, dataset: Dataset):
        self.session.add(dataset)
        self.session.commit()
        self.session.refresh(dataset)
        return dataset

    def dataset_list(self, skip: int = 0, limit: int = 10) -> DatasetListResults:
        # 查询总数
        total = self.session.exec(select(func.count(Dataset.id))).first()

        # 查询当前分页的数据
        statement = select(Dataset).offset(skip).limit(limit)
        results = self.session.exec(statement).all()
        return DatasetListResults(total=total, list=results)

    def get_dataset(self, dataset_id: str):
        statement = select(Dataset).where(Dataset.id == dataset_id)
        results = self.session.exec(statement)
        return results.first()

    def update_dataset(self, dataset_id: str, **kwargs):
        dataset = self.get_dataset(dataset_id)
        if not dataset:
            return None
        for key, value in kwargs.items():
            setattr(dataset, key, value)
        self.session.add(dataset)
        self.session.commit()
        self.session.refresh(dataset)
        return dataset

    def delete_dataset(self, dataset_id: str):
        dataset = self.get_dataset(dataset_id)
        if not dataset:
            return None
        self.session.delete(dataset)
        self.session.commit()
        return dataset_id