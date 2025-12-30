from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    content: str


class TodoUpdate(BaseModel):
    title: str | None
    content: str | None
    is_completed: bool | None
