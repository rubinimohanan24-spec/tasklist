from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Task API is running"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added", "task": task}

@app.delete("/tasks")
def delete_task(task: str):
    if task in tasks:
        tasks.remove(task)
        return {"message": "Task deleted", "task": task}
    return {"message": "Task not found"}
