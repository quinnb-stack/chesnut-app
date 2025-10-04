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


def get_customers(
    db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100
):
    customers = db.query(models.Customer)

    sortable_columns = {"id": models.Customer.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = customers.order_by(sort).offset(skip).limit(limit).all()
    return db_item


def update_customer(db: Session, user_id: int, customer: schemas.CustomerCreate):
    db_item = db.query(models.Customer).get(user_id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Customer not found.")

    db_item.behavioral_score = customer.behavioral_score
    db_item.cancel_count = customer.cancel_count

    db.commit()
    db.refresh(db_item)
    return db_item
