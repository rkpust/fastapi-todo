from fastapi import FastAPI
from todos import todos

api = FastAPI()

@api.get('/')
def index():
    return {"message": "Welcome to the FastAPI based ToDo app."}

@api.get('/todos')
def get_todos(first_n: int = None, last_n: int = None,):
    if first_n and last_n:
        # /todos?first_n=2&last_n=4
        return {
            "message": f"From {first_n} to {last_n} todo list",
            "todos": todos[first_n-1:last_n]
            }
    elif first_n:
        # /todos?first_n=2
        return {
            "message": f"First {first_n} todo list",
            "todos": todos[:first_n]
            }
    elif last_n:
        # /todos?last_n=4
        return {
            "message": f"Last {last_n} todo list",
            "todos": todos[-last_n:]
            }
    else:
        # /todos
        return {
            "message": "All todo list",
            "todos": todos
            }

# /todos/1
@api.get('/todos/{id}')
def get_todo(id: int):
    for todo in todos:
        if todo['id'] == id:
            return {
                "message": "A todo information",
                "todo": todo
                }
        
    return {
    "message": "No todo found",
    }

@api.post('/todos')
def get_todos(todo: dict):
    new_todo_id = max([todo['id'] for todo in todos]) + 1
    new_todo = {
        "id": new_todo_id,
        "name": todo['name'],
        "description": todo['description']
    }

    todos.append(new_todo)

    return {
        "message": f"A new todo is created successfully",
        "todo": new_todo
        }

@api.put('/todos/{id}')
def update_todo(id: int, updated_todo: dict):
    for todo in todos:
        if todo['id'] == id:
            todo['name'] = updated_todo['name']
            todo['description'] = updated_todo['description']

            return {
                "message": "A todo is updated successfully",
                "todo": todo
                }
        
    return {
        "message": "No todo is found for updating",
        }
       
@api.delete('/todos/{id}')
def delete_todo(id: int):
    for index, todo in enumerate(todos):
        if todo['id'] == id:
            deleted_todo = todos.pop(index)

            return {
                "message": "A todo is deleted successfully",
                "todo": deleted_todo
                }

    return {
        "message": "No todo is found for deleting",
        }
