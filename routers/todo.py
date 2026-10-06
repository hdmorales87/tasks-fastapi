from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from schemas.todo import TodoCreate, TodoUpdate
from services import todo_service


router = APIRouter(prefix="/todos")

@router.get("/")
def get_todos(
    db: Session = Depends(get_db)
):
    todos = todo_service.get_todos(db)
    return todos

@router.get("/{todo_id}")
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    todo = todo_service.get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    return todo

@router.post("/")
def create_todo(
    todo_data: TodoCreate,
    db: Session = Depends(get_db)
):
    todo = todo_service.create_todo(db, todo_data)
    return todo

@router.put("/{todo_id}")
def update_todo(
    todo_id: int,
    todo_data: TodoUpdate,
    db: Session = Depends(get_db)
):
    todo = todo_service.update_todo(
        db,
        todo_id,
        todo_data
    )
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    return todo

@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    todo = todo_service.delete_todo(db, todo_id)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    return {"message": "Todo deleted"}