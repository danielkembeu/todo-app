from fastapi.responses import JSONResponse
from fastapi import HTTPException, Query
from typing import Annotated
from fastapi import APIRouter, Response, status
from sqlmodel import select

from database.db import SessionDep
from api.v1.schemas.todo import TodoCreate, TodoUpdate
from models.todo import Todo
from utils.generate_response_messages import generate_response_message
import os

db_url = os.getenv('DATABASE_URL')
print(db_url)

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", response_model=list[Todo], responses=generate_response_message())
def read_todos(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    statement = select(Todo).offset(offset).limit(limit)
    todos_list = session.exec(statement).all()

    if not todos_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Aucune information enregistrée"},
        )

    return todos_list


@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED, responses=generate_response_message(msg="Erreur dans la creation"),)
def create_todo(session: SessionDep, todo: TodoCreate):
    new_todo = Todo(**todo.model_dump())
    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)

    return new_todo


@router.get("/{todo_id}")
def read_one_todo(todo_id: int, session: SessionDep):
    todo = session.get(Todo, todo_id)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Todo non trouvé"},
        )
    return todo


@router.put("/{todo_id}", response_model=Todo, status_code=status.HTTP_200_OK)
def update_todo(todo_id: int, session: SessionDep, update: TodoUpdate):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail={"message": "Todo non trouvé"})

    for key, value in update.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)

    session.commit()
    session.refresh(todo)

    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, session: SessionDep):
    todo = session.get(Todo, todo_id)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Todo non trouvé"},
        )

    session.delete(todo)
    session.commit()

    return {"message": "Todo supprimé avec succès"}
