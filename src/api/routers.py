from src.api.user import router as user_router
from src.api.post import router as post_pouter


all_routers = [
    user_router,
    post_pouter
]