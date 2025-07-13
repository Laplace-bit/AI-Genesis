from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class AIEventBase(BaseModel):
    title: str
    time: str
    description: str
    image_url: str
    link: str
    tags: str

class AIEventCreate(AIEventBase):
    pass

class AIEvent(AIEventBase):
    id: int

    class Config:
        orm_mode = True

class PromptBase(BaseModel):
    title: str
    prompt: str
    negative_prompt: str | None = None
    model: str
    preview_image_url: str
    parameters: str | None = None
    notes: str | None = None
    tags: str | None = None

class PromptCreate(PromptBase):
    pass

class Prompt(PromptBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
