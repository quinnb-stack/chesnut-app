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
