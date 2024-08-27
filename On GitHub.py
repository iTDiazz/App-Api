from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

list_tasks = [
    {'id': 1, 'description': 'Awake', 'status': None},
    {'id': 2, 'description': 'Have breakfast', 'status': None},
    {'id': 3, 'description': 'Take a walk', 'status': None},
    {'id': 4, 'description': 'Go to school', 'status': None}
]

class Task(BaseModel):
    id: int
    description: str
    status: Optional[bool] = None

@app.post("/tasks")
async def create_task(task: Task):
    list_tasks.append(task.dict())
    return {'operation': 'Successfully', 'data': list_tasks}

@app.get("/tasks")
async def all_tasks():
    return list_tasks

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, status: bool):
    for task in list_tasks:
        if task['id'] == task_id:
            task['status'] = status
            return {'operation': 'Successfully', 'data': task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in list_tasks:
        if task['id'] == task_id:
            list_tasks.remove(task)
            return {'operation': 'Successfully', 'data': list_tasks}
    raise HTTPException(status_code=404, detail="Task not found")
