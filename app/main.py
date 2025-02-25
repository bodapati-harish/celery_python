# app/main.py
from fastapi import FastAPI, BackgroundTasks
from app.tasks import send_email_task, process_data_task

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Celery with FastAPI!"}

@app.get("/send-email/")
def send_email(background_tasks: BackgroundTasks, email: str):
    """Trigger an email-sending task."""
    background_tasks.add_task(send_email_task, email=email)
    return {"message": f"Email to {email} is being sent!"}

@app.get("/process-data/")
def process_data(background_tasks: BackgroundTasks, data_id: int):
    """Trigger a data processing task."""
    background_tasks.add_task(process_data_task, data_id=data_id)
    return {"message": f"Data processing started for ID: {data_id}"}
