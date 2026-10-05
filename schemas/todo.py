from pydantic import BaseModel


class TodoCreate(BaseModel):
    text: str
    is_done: bool = False


class TodoUpdate(BaseModel):
    text: str | None = None
    is_done: bool = False