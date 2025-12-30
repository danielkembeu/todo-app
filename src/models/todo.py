from datetime import datetime as dt
from sqlmodel import Field, SQLModel


class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    is_completed: bool = Field(default=False, index=True)
    created_at: dt = Field(default_factory=dt.now)
