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

@router.post("/timeline/", response_model=schemas.TimelineEvent)
def create_timeline_event(event: schemas.TimelineEventCreate, db: Session = Depends(get_db)):
    return crud.create_timeline_event(db=db, event=event)

@router.get("/timeline/", response_model=List[schemas.TimelineEvent])
def read_timeline_events(skip: int = 0, limit: int = 100, tags: str = None, db: Session = Depends(get_db)):
    events = crud.get_timeline_events(db, skip=skip, limit=limit)
    if tags:
        tag_list = [tag.strip() for tag in tags.split(',')]
        events = [event for event in events if any(tag in event.tags for tag in tag_list)]
    return events

@router.get("/timeline/{event_id}", response_model=schemas.TimelineEvent)
def read_timeline_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_timeline_event(db, event_id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
