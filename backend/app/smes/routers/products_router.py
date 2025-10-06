from sqlalchemy.orm import Session

from app.smes import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/products", tags=["Products Resources"])

get_db = DatabaseSessionMaker("smes_db")


@router.get("/")
async def read_products(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_products(
        db=db, sort_direction=sort_direction, skip=skip, limit=limit
    )


@router.post("/")
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):

    return crud.create_product(db=db, product=product)


@router.put("/{id}", response_model=schemas.ProductBase)
async def update_product(
    product: schemas.ProductCreate, id: int, db: Session = Depends(get_db)
):
    return crud.update_product(db=db, id=id, product=product)


@router.delete("/{id}", response_model=schemas.ProductBase)
async def delete_product(id: int, db: Session = Depends(get_db)):

    return crud.delete_product(db=db, id=id)
