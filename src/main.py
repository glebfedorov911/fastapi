from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead
from operations.router import router as router_operation
from tasks.router import router as router_tasks
from pages.router import router as router_pages
from chat.router import router as router_chat
from auth.router import router as router_role

from config import REDIS_HOST, REDIS_PORT

app = FastAPI(
    title="Trading App"
)

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)
app.include_router(router_tasks)
app.include_router(router_pages)
app.include_router(router_chat)
app.include_router(router_role)


origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type', 'Set-Cookie', 'Access-Control-Allow-Headers', 'Access-Control-Allow-Origin'],
)

@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
