from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def welcome():
    return {"Hello": "World"}

@app.get("/api/tasks")
async def get_task():
    return "all task"

#@app.get(f'/api/tasks/{id}')
@app.get("/api/tasks/{id}")
async def get_tasks():
    return "single task"

@app.post("/api/tasks")
async def create_task():
    pass

@app.put("/api/tasks/{id}")
async def update_task():
    pass

@app.delete("/api/tasks/{id}")
async def delete_task():
    pass