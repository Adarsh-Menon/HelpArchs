from fastapi import FastAPI
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel , Field


api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1
    
class todo(BaseModel):
    todo_id: int
    todo_name: str = Field(..., title="Todo Name", max_length=50)
    todo_description: Optional[str] = Field(None, title="Todo Description", max_length=100)
    priority: Priority = Field(Priority.LOW, title="Priority")
    completed: bool = Field(False, title="Completed")

all_todos = [
    {'todo_id': 1,'name':'Sports','description':'Play football','completed':False},
    {'todo_id': 2,'name':'Sports','description':'Play cricket','completed':False},
    {'todo_id': 3,'name':'Sports','description':'Play baseball','completed':False},
    {'todo_id': 4,'name':'Sports','description':'Play handball','completed':False},
    {'todo_id': 5,'name':'Sports','description':'Play  snooker','completed':False},
]


#POST , GET , PUT, DELETE
@api.get("/")
def index():
    return {"message":"Hello World"}


#localhost:8000/todos/2
@api.get('/todos/{todo_id}')
def get_todo(todo_id:int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {"result":todo}
    return {"message":"Todo not found"}



#localhost:8000/todos?first_n=2

@api.get('/todos')
def get_todo(first_n:int = None):
    if first_n:
        return{"result":all_todos[:first_n]}
    else:
        return {"result":all_todos}


@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1
    
    new_todo = {
        'todo_id' : new_todo_id,
        'todo_name' : todo['todo_name'],
        'todo_description' : todo['todo_description'],
    }
    
    all_todos.append(new_todo)
    return {"result":new_todo}