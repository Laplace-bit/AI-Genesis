from sqlalchemy.orm import Session
from . import models, schemas

def get_timeline_event(db: Session, event_id: int):
    return db.query(models.TimelineEvent).filter(models.TimelineEvent.id == event_id).first()

def get_timeline_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TimelineEvent).offset(skip).limit(limit).all()

def create_timeline_event(db: Session, event: schemas.TimelineEventCreate):
    db_event = models.TimelineEvent(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
