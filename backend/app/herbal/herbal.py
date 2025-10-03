from fastapi import FastAPI
from app.database import DatabaseSessionMaker
from app.herbal.routers import (
    user_router,
    herbal_plants_router,
    brgy_router,
    plant_geotag_router,
    logs_router,
)

app = FastAPI()

get_db = DatabaseSessionMaker("herbal_db")

app.include_router(user_router.router)
app.include_router(herbal_plants_router.router)
app.include_router(brgy_router.router)
app.include_router(plant_geotag_router.router)
app.include_router(logs_router.router)
