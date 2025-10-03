from sqlalchemy.orm import Session

from app.herbal import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/geotag", tags=["Herbal Plant Geotag Resources"])

get_db = DatabaseSessionMaker("herbal_db")


@router.get("/")
async def read_geotags(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
    plant_id: int = None,
    brgy_id: int = None,
    user_id: int = None,
):
    return crud.get_geotags(
        db=db,
        sort_direction=sort_direction,
        skip=skip,
        limit=limit,
        plant_id=plant_id,
        brgy_id=brgy_id,
        user_id=user_id,
    )


@router.post("/")
async def create_geotag(
    geotag: schemas.PlantGeotagCreate, db: Session = Depends(get_db)
):

    return crud.create_geotag(db=db, geotag=geotag)


@router.put("/{id}", response_model=schemas.PlantGeotagBase)
async def update_geotag(
    geotag: schemas.PlantGeotagCreate, id: int, db: Session = Depends(get_db)
):
    return crud.update_geotag(db=db, id=id, geotag=geotag)


@router.delete("/{id}", response_model=schemas.PlantGeotagBase)
async def delete_geotag(id: int, db: Session = Depends(get_db)):

    return crud.delete_geotag(db=db, id=id)
