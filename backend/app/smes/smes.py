from fastapi import FastAPI
from app.database import DatabaseSessionMaker
from app.smes.routers import (
    user_router,
    customers_router,
    branches_router,
    riders_router,
    products_router,
)

app = FastAPI()

get_db = DatabaseSessionMaker("smes_db")

app.include_router(user_router.router)
app.include_router(customers_router.router)
app.include_router(branches_router.router)
app.include_router(riders_router.router)
app.include_router(products_router.router)
