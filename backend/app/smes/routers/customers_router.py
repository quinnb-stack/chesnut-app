from sqlalchemy.orm import Session

from app.smes import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/customers", tags=["Customers Resources"])

get_db = DatabaseSessionMaker("smes_db")


@router.get("/")
async def read_customers(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_customers(
        db=db, sort_direction=sort_direction, skip=skip, limit=limit
    )


@router.put("/{user_id}", response_model=schemas.CustomerBase)
async def update_customer(
    customer: schemas.CustomerCreate, user_id: int, db: Session = Depends(get_db)
):
    return crud.update_customer(db=db, user_id=user_id, customer=customer)
