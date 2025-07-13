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

class UserCreate(UserBase):
    username: str
    password: str

class User(UserBase):
    id: int
    username: str
    is_active: bool
    prompts: list[Prompt] = []

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
