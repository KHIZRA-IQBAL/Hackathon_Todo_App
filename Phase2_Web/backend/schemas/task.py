from typing import Optional
from sqlmodel import SQLModel

class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(SQLModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    user_id: int
