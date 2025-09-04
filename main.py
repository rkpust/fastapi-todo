from fastapi import FastAPI

api = FastAPI()

@api.get('/')
def index():
    return {"message": "Welcome to the FastAPI based ToDo app."}
