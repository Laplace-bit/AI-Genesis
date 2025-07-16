from sqlalchemy.orm import Session
import models, schemas

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

def get_tutorial(db: Session, tutorial_id: int):
    return db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).first()

def get_tutorials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tutorial).offset(skip).limit(limit).all()

def create_tutorial(db: Session, tutorial: schemas.TutorialCreate):
    db_tutorial = models.Tutorial(**tutorial.dict())
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

def get_prompt(db: Session, prompt_id: int):
    return db.query(models.Prompt).filter(models.Prompt.id == prompt_id).first()

def get_prompts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Prompt).offset(skip).limit(limit).all()

def create_prompt(db: Session, prompt: schemas.PromptCreate, author_id: int):
    db_prompt = models.Prompt(**prompt.dict(), author_id=author_id)
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    from security import get_password_hash
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: models.User, user_update: schemas.UserUpdate):
    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_comment(db: Session, comment: schemas.CommentCreate, author_id: int):
    db_comment = models.Comment(**comment.dict(), author_id=author_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_for_tutorial(db: Session, tutorial_id: int):
    return db.query(models.Comment).filter(models.Comment.tutorial_id == tutorial_id).all()
