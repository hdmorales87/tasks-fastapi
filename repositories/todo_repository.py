from sqlalchemy.orm import Session
from models.todo import Todo

def find_all(db: Session):
    return db.query(Todo).all()

def find_by_id(db: Session, todo_id: int):
    return (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .first()
    )

def create(db: Session, todo: Todo):
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update(db: Session, todo: Todo):
    db.commit()
    db.refresh(todo)
    return todo

def delete(db: Session, todo: Todo):
    db.delete(todo)
    db.commit()