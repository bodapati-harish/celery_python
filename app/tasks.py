# app/tasks.py
from celery import Celery
import time

# Initialize Celery
celery_app = Celery(
    "app.tasks",
    broker="redis://redis:6379/0",  # Redis as the message broker
    backend="redis://redis:6379/0"  # Redis as the result backend
)

@celery_app.task(name="send_email_task")
def send_email_task(email: str):
    """Simulate sending an email."""
    print(f"Sending email to {email}...")
    time.sleep(5)  # Simulate delay
    print("Email sent!")
    return f"Email sent to {email}"

@celery_app.task(name="process_data_task")
def process_data_task(data_id: int):
    """Simulate data processing."""
    print(f"Processing data with ID: {data_id}...")
    time.sleep(10)  # Simulate delay
    print("Data processed!")
    return f"Data processed for ID: {data_id}"
