from sqlalchemy.orm import Session

from app.herbal import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/brgys", tags=["Barangays Resources"])

get_db = DatabaseSessionMaker("herbal_db")


@router.get("/")
async def read_brgys(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_brgys(db=db, sort_direction=sort_direction, skip=skip, limit=limit)


@router.post("/")
async def create_brgy(brgy: schemas.BarangayCreate, db: Session = Depends(get_db)):

    return crud.create_brgy(db=db, brgy=brgy)


@router.put("/{id}", response_model=schemas.BarangayBase)
async def update_brgy(
    brgy: schemas.BarangayCreate, id: int, db: Session = Depends(get_db)
):
    return crud.update_brgy(db=db, id=id, brgy=brgy)


@router.delete("/{id}", response_model=schemas.BarangayBase)
async def delete_brgy(id: int, db: Session = Depends(get_db)):

    return crud.delete_brgy(db=db, id=id)
