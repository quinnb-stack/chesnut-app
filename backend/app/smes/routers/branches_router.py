from typing import List
from sqlalchemy.orm import Session

from app.smes import crud, schemas
from app.database import DatabaseSessionMaker
from fastapi import APIRouter, Depends, File, Header, HTTPException, UploadFile

router = APIRouter(prefix="/branches", tags=["Branches Resources"])

get_db = DatabaseSessionMaker("smes_db")


@router.get("/")
async def read_branches(
    db: Session = Depends(get_db),
    sort_direction: str = "desc",
    skip: int = 0,
    limit: int = 100,
):
    return crud.get_branches(
        db=db, sort_direction=sort_direction, skip=skip, limit=limit
    )


@router.post("/")
async def create_branch(branch: schemas.BranchCreate, db: Session = Depends(get_db)):

    return crud.create_branch(db=db, branch=branch)


@router.put("/{id}", response_model=schemas.BranchBase)
async def update_branch(
    branch: schemas.BranchCreate, id: int, db: Session = Depends(get_db)
):
    return crud.update_branch(db=db, id=id, branch=branch)


@router.delete("/{id}", response_model=schemas.BranchBase)
async def delete_branch(id: int, db: Session = Depends(get_db)):

    return crud.delete_branch(db=db, id=id)


@router.get("/{branch_id}/products")
def get_branch_products(branch_id: int, db: Session = Depends(get_db)):
    return crud.get_branch_products(db, branch_id)


@router.post("/{branch_id}/products")
async def create_branch_product(
    branch_product: schemas.BranchProductCreate, db: Session = Depends(get_db)
):

    return crud.create_branch_product(db=db, branch_product=branch_product)
