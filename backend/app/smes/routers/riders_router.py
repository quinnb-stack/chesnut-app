from sqlalchemy.orm import Session

from app.smes import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/riders", tags=["Riders Resources"])

get_db = DatabaseSessionMaker("smes_db")


@router.get("/")
async def read_riders(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_riders(db=db, sort_direction=sort_direction, skip=skip, limit=limit)


@router.post("/")
async def assign_rider(rider: schemas.RiderCreate, db: Session = Depends(get_db)):

    return crud.assign_rider(db=db, rider=rider)


@router.put("/{user_id}", response_model=schemas.RiderBase)
async def re_assign_rider(
    rider: schemas.RiderCreate, user_id: int, db: Session = Depends(get_db)
):
    return crud.re_assign_rider(db=db, user_id=user_id, rider=rider)


@router.delete("/{id}", response_model=schemas.RiderBase)
async def delete_rider(id: int, db: Session = Depends(get_db)):

    return crud.delete_rider(db=db, id=id)
