import uvicorn
from fastapi import FastAPI

from config import config
from routers.app import app_router
from routers.dataset import dataset_router
from routers.provider import provider_router
from routers.user import user_router

app = FastAPI(
    title=config.APP_NAME,
    version='0.0.1',
    root_path='/api/v1',
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

app.include_router(app_router, prefix='/apps', tags=['App'])
app.include_router(user_router, prefix='/users', tags=['User'])
app.include_router(dataset_router, prefix='/datasets', tags=['Dataset'])
app.include_router(provider_router, prefix='/providers', tags=['Provider'])

if __name__ == '__main__':
    uvicorn.run('app:app')