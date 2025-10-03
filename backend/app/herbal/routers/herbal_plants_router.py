from sqlalchemy.orm import Session

from app.herbal import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/herbal", tags=["Herbal Plant Resources"])

get_db = DatabaseSessionMaker("herbal_db")


@router.get("/")
async def read_herbals(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_herbals(
        db=db, sort_direction=sort_direction, skip=skip, limit=limit
    )


@router.post("/")
async def create_herbal(
    herbal: schemas.HerbalPlantCreate, db: Session = Depends(get_db)
):

    return crud.create_herbal(db=db, herbal=herbal)


@router.put("/{id}", response_model=schemas.HerbalPlantBase)
async def update_herbal(
    herbal: schemas.HerbalPlantCreate, id: int, db: Session = Depends(get_db)
):
    return crud.update_herbal(db=db, id=id, herbal=herbal)


@router.delete("/{id}", response_model=schemas.HerbalPlantBase)
async def delete_herbal(id: int, db: Session = Depends(get_db)):

    return crud.delete_herbal(db=db, id=id)
