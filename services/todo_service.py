from sqlalchemy.orm import Session
from models.todo import Todo
from repositories import todo_repository
from schemas.todo import TodoCreate, TodoUpdate

def get_todos(db: Session):
    return todo_repository.find_all(db)

def get_todo(db: Session, todo_id: int):
    return todo_repository.find_by_id(db, todo_id)

def create_todo(db: Session, todo_data: TodoCreate):
    todo = Todo(
        text=todo_data.text,
        is_done=todo_data.is_done
    )
    return todo_repository.create(db, todo)

def update_todo(
    db: Session,
    todo_id: int,
    todo_data: TodoUpdate
):
    todo = todo_repository.find_by_id(db, todo_id)
    if todo is None:
        return None
    if todo_data.text:
        todo.text = todo_data.text
    todo.is_done = todo_data.is_done
    return todo_repository.update(db, todo)

def delete_todo(db: Session, todo_id: int):
    todo = todo_repository.find_by_id(db, todo_id)
    if todo is None:
        return None
    todo_repository.delete(db, todo)
    return todo