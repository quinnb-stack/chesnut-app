from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException


def get_users(
    db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100
):
    users = db.query(models.User)

    sortable_columns = {"id": models.User.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = users.order_by(sort).offset(skip).limit(limit).all()
    return db_item


def get_herbals(
    db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100
):
    herbals = db.query(models.HerbalPlant)

    sortable_columns = {"id": models.HerbalPlant.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = herbals.order_by(sort).offset(skip).limit(limit).all()
    return db_item


def create_herbal(db: Session, herbal: schemas.HerbalPlantCreate):
    query = (
        db.query(models.HerbalPlant)
        .filter(models.HerbalPlant.name == herbal.name)
        .filter(models.HerbalPlant.is_deleted == 0)
        .first()
    )

    if query:
        raise HTTPException(status_code=400, detail="Herbal plant already exist.")

    db_item = models.HerbalPlant(**herbal.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_herbal(db: Session, id: int, herbal: schemas.HerbalPlantCreate):
    db_item = db.query(models.HerbalPlant).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Herbal plant not found.")

    db_item.name = herbal.name
    db_item.scientific_name = herbal.scientific_name
    db_item.description = herbal.description
    db_item.image_url = herbal.image_url
    db_item.is_deleted = herbal.is_deleted

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_herbal(db: Session, id: int):
    db_item = db.query(models.HerbalPlant).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Herbal plant not found.")

    db_item.is_deleted = 1

    db.commit()
    db.refresh(db_item)
    return db_item


def get_brgys(
    db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100
):
    brgys = db.query(models.Barangay)

    sortable_columns = {"id": models.Barangay.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = brgys.order_by(sort).offset(skip).limit(limit).all()
    return db_item


def create_brgy(db: Session, brgy: schemas.BarangayCreate):
    query = (
        db.query(models.Barangay)
        .filter(models.Barangay.name == brgy.name)
        .filter(models.Barangay.is_deleted == 0)
        .first()
    )

    if query:
        raise HTTPException(status_code=400, detail="Barangay already exist.")

    db_item = models.Barangay(**brgy.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_brgy(db: Session, id: int, brgy: schemas.BarangayCreate):
    db_item = db.query(models.Barangay).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Barangay not found.")

    db_item.name = brgy.name
    db_item.municipality = brgy.municipality
    db_item.captain_official = brgy.captain_official
    db_item.is_deleted = brgy.is_deleted

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_brgy(db: Session, id: int):
    db_item = db.query(models.Barangay).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Barangay not found.")

    db_item.is_deleted = 1

    db.commit()
    db.refresh(db_item)
    return db_item


def get_geotags(
    db: Session,
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
    plant_id=None,
    brgy_id=None,
    user_id=None,
):
    geotags = db.query(models.PlantGeotag)

    if plant_id is not None:
        geotags = geotags.filter(models.PlantGeotag.plant_id == plant_id)
    if brgy_id is not None:
        geotags = geotags.filter(models.PlantGeotag.brgy_id == brgy_id)
    if user_id is not None:
        geotags = geotags.filter(models.PlantGeotag.user_id == user_id)

    sortable_columns = {"id": models.PlantGeotag.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = geotags.order_by(sort).offset(skip).limit(limit).all()
    return db_item


def create_geotag(db: Session, geotag: schemas.PlantGeotagCreate):
    query = (
        db.query(models.PlantGeotag)
        .filter(models.PlantGeotag.plant_id == geotag.plant_id)
        .filter(models.PlantGeotag.latitude == geotag.latitude)
        .filter(models.PlantGeotag.longitude == geotag.longitude)
        .first()
    )

    if query:
        raise HTTPException(status_code=400, detail="PlantGeotag already exist.")

    db_item = models.PlantGeotag(**geotag.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_geotag(db: Session, id: int, geotag: schemas.PlantGeotagCreate):
    db_item = db.query(models.PlantGeotag).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="PlantGeotag not found.")

    db_item.latitude = geotag.latitude
    db_item.longitude = geotag.longitude

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_geotag(db: Session, id: int):
    db_item = db.query(models.PlantGeotag).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="PlantGeotag not found.")

    db.delete(db_item)
    db.commit()
    return db_item


def get_logs(
    db: Session,
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
    user_id=None,
):
    logs = db.query(models.Log)

    if user_id is not None:
        logs = logs.filter(models.Log.user_id == user_id)

    sortable_columns = {"id": models.Log.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = logs.order_by(sort).offset(skip).limit(limit).all()
    return db_item
