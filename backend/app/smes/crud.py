from sqlalchemy.orm import Session, joinedload
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


def get_branches(
    db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100
):
    branches = db.query(models.Branch)

    sortable_columns = {"id": models.Branch.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = branches.order_by(sort).offset(skip).limit(limit).all()
    return db_item


def create_branch(db: Session, branch: schemas.BranchCreate):
    query = (
        db.query(models.Branch)
        .filter(models.Branch.name == branch.name)
        .filter(models.Branch.is_deleted == 0)
        .first()
    )

    if query:
        raise HTTPException(status_code=409, detail="Branch already exist.")

    db_item = models.Branch(**branch.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_branch(db: Session, id: int, branch: schemas.BranchCreate):
    db_item = db.query(models.Branch).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Branch not found.")

    db_item.user_id = branch.user_id
    db_item.name = branch.name
    db_item.address = branch.address
    db_item.is_deleted = branch.is_deleted

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_branch(db: Session, id: int):
    db_item = db.query(models.Branch).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Branch not found.")

    db_item.is_deleted = 1

    db.commit()
    db.refresh(db_item)
    return db_item


def get_branch_products(db: Session, branch_id: int):

    branch = (
        db.query(models.Branch)
        .options(
            joinedload(models.Branch.branch_products).joinedload(
                models.BranchProduct.product
            )
        )
        .filter(models.Branch.id == branch_id)
        .first()
    )

    if branch is None:
        raise HTTPException(status_code=404, detail="Branch not found.")

    branch_data = {
        "id": branch.id,
        "name": branch.name,
        "address": branch.address,
        "user_id": branch.user_id,
        "is_deleted": branch.is_deleted,
        "products": [],
    }

    for bp in branch.branch_products:
        if bp.product and bp.product.is_deleted == 0:
            branch_data["products"].append(
                {
                    "id": bp.product.id,
                    "name": bp.product.name,
                    "price": bp.product.price,
                    "description": bp.product.description,
                    "image": bp.product.image,
                    "quantity": bp.quantity,
                    "is_deleted": bp.product.is_deleted,
                }
            )

    return branch_data


def create_branch_product(db: Session, branch_product: schemas.BranchProductCreate):
    query = (
        db.query(models.BranchProduct)
        .filter(models.BranchProduct.product_id == branch_product.product_id)
        .first()
    )

    if query:
        raise HTTPException(status_code=409, detail="Branch product already exist.")

    db_item = models.BranchProduct(**branch_product.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_riders(
    db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100
):
    riders = db.query(models.Rider)

    sortable_columns = {"id": models.Rider.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = riders.order_by(sort).offset(skip).limit(limit).all()
    return db_item


def assign_rider(db: Session, rider: schemas.RiderCreate):
    query = (
        db.query(models.Rider)
        .filter(models.Rider.branch_id == rider.branch_id)
        .filter(models.Rider.is_deleted == 0)
        .first()
    )

    if query:
        raise HTTPException(
            status_code=409, detail="Rider already assigned to your branch."
        )

    db_item = models.Rider(**rider.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def re_assign_rider(db: Session, user_id: int, rider: schemas.RiderCreate):
    db_item = db.query(models.Rider).filter(models.Rider.user_id == user_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail="Rider not found.")

    db_item.branch_id = rider.branch_id
    db_item.is_deleted = rider.is_deleted

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_rider(db: Session, id: int):
    db_item = db.query(models.Rider).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Rider not found.")

    db_item.is_deleted = 1

    db.commit()
    db.refresh(db_item)
    return db_item


def get_products(
    db: Session, sort_direction: str = "desc", skip: int = 0, limit: int = 100
):
    products = db.query(models.Product)

    sortable_columns = {"id": models.Product.id}

    sort = (
        sortable_columns.get("id").desc()
        if sort_direction == "desc"
        else sortable_columns.get("id").asc()
    )

    db_item = products.order_by(sort).offset(skip).limit(limit).all()
    return db_item


def create_product(db: Session, product: schemas.ProductCreate):
    query = (
        db.query(models.Product)
        .filter(models.Product.name == product.name)
        .filter(models.Product.is_deleted == 0)
        .first()
    )

    if query:
        raise HTTPException(status_code=409, detail="Product already exist.")

    db_item = models.Product(**product.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_product(db: Session, id: int, product: schemas.ProductCreate):
    db_item = db.query(models.Product).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Product not found.")

    db_item.name = product.name
    db_item.price = product.price
    db_item.image = product.image
    db_item.description = product.description
    db_item.is_deleted = product.is_deleted

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_product(db: Session, id: int):
    db_item = db.query(models.Product).get(id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Product not found.")

    db_item.is_deleted = 1

    db.commit()
    db.refresh(db_item)
    return db_item
