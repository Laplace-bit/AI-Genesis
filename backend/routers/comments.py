from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import SessionLocal
from ..routers.auth import get_current_user

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_comment(db=db, comment=comment, author_id=current_user.id)

@router.get("/tutorials/{tutorial_id}/comments/", response_model=List[schemas.Comment])
def read_comments_for_tutorial(tutorial_id: int, db: Session = Depends(get_db)):
    comments = crud.get_comments_for_tutorial(db, tutorial_id=tutorial_id)
    return comments
