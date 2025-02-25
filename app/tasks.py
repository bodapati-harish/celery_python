from celery import Celery

# Initialize Celery with Redis as the broker
app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

@app.task
def add(x, y):
    return x + y

@app.task
def subtract(x, y):
    return x - y

@app.task
def multiply(x, y):
    return x * y

@app.task
def divide(x, y):
    return x / y if y != 0 else 'Error: Division by zero'
