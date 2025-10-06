from sqlalchemy.orm import Session

from app.smes import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/users", tags=["Users Resources"])

get_db = DatabaseSessionMaker("smes_db")


@router.get("/")
async def read_users(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_users(db=db, sort_direction=sort_direction, skip=skip, limit=limit)
