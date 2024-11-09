from src.api.user import router as user_router
from src.api.post import router as post_pouter
from src.api.admin import router as admin_router
from src.api.institution import router as inst_router


all_routers = [
    user_router,
    post_pouter,
    admin_router,
    inst_router
]