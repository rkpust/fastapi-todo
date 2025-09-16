from enum import IntEnum
from pydantic import BaseModel, Field

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1 

class ToDoBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=512, description="Name of the ToDo")
    description: str = Field(..., description="Description of the ToDo")
    priority: Priority = Field(default=Priority.LOW, description="Priority of the ToDo")

class ToDoCreate(ToDoBase):
    pass

class ToDo(ToDoBase):
    id: int = Field(..., description="Unique indentifier of the ToDo")

class ToDoUpdate(BaseModel):
    name: str = Field(None, min_length=3, max_length=512, description="Name of the ToDo")
    description: str = Field(None, description="Description of the ToDo")
    priority: Priority = Field(None, description="Priority of the ToDo")

todos = [
    ToDo(id=1, name='Sports', description='Go to gym', priority=Priority.HIGH),
    ToDo(id=2, name='Read', description='Read 10 minute', priority=Priority.LOW),
    ToDo(id=3, name='Shop', description='Go Shoping'),
    ToDo(id=4, name='Study', description='Study for exam', priority=Priority.HIGH),
    ToDo(id=5, name='Break', description='Break for 10 minute', priority=Priority.MEDIUM),
    ToDo(id=6, name='Code', description='Coding for project', priority=Priority.HIGH)
]
