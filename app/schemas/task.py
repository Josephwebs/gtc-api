from datetime import datetime, date
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str | None = None
    due_date: date | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
