from fastapi import FastAPI

from src.api.routers import all_routers
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Хеллоу Мария'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in all_routers:
    app.include_router(router)