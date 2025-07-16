from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud, models, schemas
from database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tutorials/", response_model=schemas.Tutorial)
def create_tutorial(tutorial: schemas.TutorialCreate, db: Session = Depends(get_db)):
    return crud.create_tutorial(db=db, tutorial=tutorial)

@router.get("/tutorials/", response_model=List[schemas.Tutorial])
def read_tutorials(skip: int = 0, limit: int = 100, category: str = None, difficulty: str = None, db: Session = Depends(get_db)):
    tutorials = crud.get_tutorials(db, skip=skip, limit=limit)
    if category:
        tutorials = [tutorial for tutorial in tutorials if tutorial.category == category]
    if difficulty:
        tutorials = [tutorial for tutorial in tutorials if tutorial.difficulty == difficulty]
    return tutorials

@router.get("/tutorials/{tutorial_id}", response_model=schemas.Tutorial)
def read_tutorial(tutorial_id: int, db: Session = Depends(get_db)):
    db_tutorial = crud.get_tutorial(db, tutorial_id=tutorial_id)
    if db_tutorial is None:
        raise HTTPException(status_code=404, detail="Tutorial not found")
    return db_tutorial
