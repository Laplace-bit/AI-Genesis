from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date, Table
from sqlalchemy.orm import relationship

from database import Base

prompt_likes = Table('prompt_likes', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('prompt_id', Integer, ForeignKey('prompts.id'), primary_key=True)
)

class TimelineEvent(Base):
    __tablename__ = "timeline_events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(Date)
    description = Column(Text)
    image_url = Column(String)
    source_url = Column(String)
    tags = Column(String) # Simple comma-separated string for now


class Tutorial(Base):
    __tablename__ = "tutorials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category = Column(String) # e.g., "by_industry", "by_task"
    subcategory = Column(String) # e.g., "Marketing", "Content Writing"
    content = Column(Text)
    difficulty = Column(String) # e.g., "Beginner", "Intermediate", "Expert"
    cover_image_url = Column(String, nullable=True)
    comments = relationship("Comment", back_populates="tutorial")


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    prompt_text = Column(Text)
    negative_prompt_text = Column(Text, nullable=True)
    model = Column(String) # e.g., "Midjourney V6", "DALL-E 3"
    preview_url = Column(String)
    tags = Column(String)
    author_id = Column(Integer, ForeignKey("users.id")) # Assuming a User model

    author = relationship("User", back_populates="prompts")
    liked_by = relationship(
        "User",
        secondary=prompt_likes,
        back_populates="liked_prompts")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    full_name = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    avatar_url = Column(String, nullable=True)

    prompts = relationship("Prompt", back_populates="author")
    liked_prompts = relationship(
        "Prompt",
        secondary=prompt_likes,
        back_populates="liked_by")
    comments = relationship("Comment", back_populates="author")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    tutorial_id = Column(Integer, ForeignKey("tutorials.id"))

    author = relationship("User")
    tutorial = relationship("Tutorial")
