from __future__ import annotations
from pydantic import BaseModel
from datetime import date

class TimelineEventBase(BaseModel):
    title: str
    date: date
    description: str
    image_url: str | None = None
    source_url: str | None = None
    tags: str | None = None

class TimelineEventCreate(TimelineEventBase):
    pass

class TimelineEvent(TimelineEventBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    full_name: str | None = None
    bio: str | None = None
    avatar_url: str | None = None

class UserCreate(UserBase):
    username: str
    password: str

class UserUpdate(UserBase):
    pass

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    tutorial_id: int

class Comment(CommentBase):
    id: int
    author_id: int
    author: 'User'

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    username: str
    is_active: bool
    prompts: list[Prompt] = []
    comments: list[Comment] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


class TutorialBase(BaseModel):
    title: str
    category: str
    subcategory: str
    content: str
    difficulty: str
    cover_image_url: str | None = None

class TutorialCreate(TutorialBase):
    pass

class Tutorial(TutorialBase):
    id: int
    comments: list[Comment] = []

    class Config:
        orm_mode = True


class PromptBase(BaseModel):
    title: str
    prompt_text: str
    negative_prompt_text: str | None = None
    model: str
    preview_url: str
    tags: str | None = None

class PromptCreate(PromptBase):
    author_id: int

class User(UserBase):
    id: int
    username: str
    is_active: bool
    prompts: list['Prompt'] = []

    class Config:
        orm_mode = True

class Prompt(PromptBase):
    id: int
    author_id: int
    liked_by: list['User'] = []

    class Config:
        orm_mode = True

User.update_forward_refs()
Prompt.update_forward_refs()
