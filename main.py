from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
from todos import todos, ToDo

api = FastAPI()

@api.get('/')
def index():
    return {"message": "Welcome to the FastAPI based ToDo app."}

@api.get('/todos', response_model=List[ToDo])
def get_todos(first_n: int = None, last_n: int = None,):
    selected_todos = None

    if first_n and last_n:
        # /todos?first_n=2&last_n=4
        selected_todos =  todos[first_n-1:last_n]
        return selected_todos
    elif first_n:
        # /todos?first_n=2
        selected_todos =  todos[:first_n]
        return selected_todos
    elif last_n:
        # /todos?last_n=4
        selected_todos =  todos[-last_n:]
        return selected_todos
    else:
        # /todos
        return todos

# /todos/1
@api.get('/todos/{id}', response_model=ToDo)
def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
        
    # Return a custom error response
    return JSONResponse(status_code=404, content={"message": "No todo found with the given ID"})
