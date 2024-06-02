import uvicorn
from fastapi import FastAPI

from config import config
from routers.app import app_router
from routers.dataset import dataset_router
from routers.provider import provider_router
from routers.user import user_router

app = FastAPI(
    title=config.APP_NAME,
    version='0.0.1'
)

app.include_router(app_router, prefix='/apps')
app.include_router(user_router, prefix='/users')
app.include_router(dataset_router, prefix='/datasets')
app.include_router(provider_router, prefix='/providers')

if __name__ == '__main__':
    uvicorn.run('app:app')