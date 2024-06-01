from sqlmodel import Session, create_engine

from config import config

engine = create_engine(str(config.DATABASE_URL), echo=True)

def get_session():
    with Session(engine) as session:
        yield session