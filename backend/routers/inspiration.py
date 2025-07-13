from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/prompts/", response_model=schemas.Prompt)
def create_prompt(prompt: schemas.PromptCreate, db: Session = Depends(get_db)):
    return crud.create_prompt(db=db, prompt=prompt)

@router.get("/prompts/", response_model=List[schemas.Prompt])
def read_prompts(skip: int = 0, limit: int = 100, type: str = None, style: str = None, db: Session = Depends(get_db)):
    prompts = crud.get_prompts(db, skip=skip, limit=limit)
    if type:
        prompts = [prompt for prompt in prompts if type in prompt.tags]
    if style:
        prompts = [prompt for prompt in prompts if style in prompt.tags]
    return prompts

@router.get("/prompts/{prompt_id}", response_model=schemas.Prompt)
def read_prompt(prompt_id: int, db: Session = Depends(get_db)):
    db_prompt = crud.get_prompt(db, prompt_id=prompt_id)
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return db_prompt
