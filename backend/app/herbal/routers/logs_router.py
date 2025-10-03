from sqlalchemy.orm import Session

from app.herbal import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/logs", tags=["Logs Resources"])

get_db = DatabaseSessionMaker("herbal_db")


@router.get("/")
async def read_logs(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
    user_id: int = None,
):
    return crud.get_logs(
        db=db,
        sort_direction=sort_direction,
        skip=skip,
        limit=limit,
        user_id=user_id,
    )
