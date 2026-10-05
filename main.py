from fastapi import FastAPI

from db import Base, engine
from routers.todo import router as todo_router


Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(todo_router)