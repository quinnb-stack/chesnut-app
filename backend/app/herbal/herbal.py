from fastapi import Depends, FastAPI
from app.database import DatabaseSessionMaker
from app.herbal import crud, schemas
from app.herbal.routers import (
    user_router,
    herbal_plants_router,
)

app = FastAPI()

get_db = DatabaseSessionMaker("herbal_db")

app.include_router(user_router.router)
app.include_router(herbal_plants_router.router)
