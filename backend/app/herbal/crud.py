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
