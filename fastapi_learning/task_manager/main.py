# =====================================================================
# TASK MANAGER PROJECT: MAIN APPLICATION ENTRY (main.py)
# =====================================================================
# Is file me hum:
# 1. User Registration & Login endpoints (OAuth2 format)
# 2. Authenticated Tasks CRUD endpoints
# 3. BackgroundTasks triggers to simulate emails on updates.
#
# RUNNING INSTRUCTIONS:
# From 'fastapi_learning' folder run: `uvicorn task_manager.main:app --reload`
# Docs URL: http://127.0.0.1:8000/docs

from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
import asyncio

# Project imports using relative module imports
from .database import db
from .schemas import (
    UserRegisterSchema, TokenResponseSchema,
    TaskCreateSchema, TaskUpdateSchema, TaskResponseSchema
)
from .auth import (
    hash_password, verify_password, create_access_token, get_current_user
)

app = FastAPI(
    title="🚀 AI Automation Hub - Task Manager API",
    description="Secure Task Management API with custom User Authentication & Background Notification Triggers.",
    version="1.0"
)

# ---------------------------------------------------------------------
# Background Task: Email Notification Simulator
# ---------------------------------------------------------------------
async def send_task_email_notification(email: str, username: str, task_title: str, action: str):
    """
    Slower SMTP transaction simulation in background.
    """
    print(f"[Email Worker] Starting email preparation for {email}...")
    await asyncio.sleep(3.0) # Simulating network lag / SMTP payload validation
    
    email_body = f"""
    ========================================
    📧 MOCK EMAIL NOTIFICATION
    To: {email}
    Subject: Task Alert for user @{username}!
    
    Dear {username},
    Your task: '{task_title}' was successfully {action.upper()}ED.
    ========================================
    """
    print(email_body)
    print(f"[Email Worker] Notification delivered successfully to {email}!\n")


# ---------------------------------------------------------------------
# Route Area: Authentication Endpoints
# ---------------------------------------------------------------------
@app.post("/auth/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserRegisterSchema):
    # Check if user already exists
    existing_user = db.get_user(user.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered. Please choose another."
        )
    
    # Hash password and save to DB
    hashed = hash_password(user.password)
    user_payload = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed
    }
    db.save_user(user_payload)
    
    return {"message": f"User @{user.username} registered successfully!"}

@app.post("/auth/login", response_model=TokenResponseSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Find user
    user = db.get_user(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create Access Token
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


# ---------------------------------------------------------------------
# Route Area: Task CRUD (Requires Authentication via get_current_user)
# ---------------------------------------------------------------------

@app.post("/tasks", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreateSchema,
    background_tasks: BackgroundTasks,
    current_user: dict = Depends(get_current_user)
):
    task_payload = {
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "status": "todo",
        "owner": current_user["username"]
    }
    created = db.create_task(task_payload)
    
    # Add background email task to worker queue
    background_tasks.add_task(
        send_task_email_notification,
        current_user["email"],
        current_user["username"],
        created["title"],
        "create"
    )
    
    return created

@app.get("/tasks", response_model=List[TaskResponseSchema])
async def list_tasks(current_user: dict = Depends(get_current_user)):
    # Authenticated user can only read their own tasks
    return db.get_user_tasks(current_user["username"])

@app.get("/tasks/{task_id}", response_model=TaskResponseSchema)
async def get_task_details(task_id: str, current_user: dict = Depends(get_current_user)):
    task = db.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    
    # Restrict read access to task owner only
    if task["owner"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not authorized to access this task.")
        
    return task

@app.put("/tasks/{task_id}", response_model=TaskResponseSchema)
async def update_task(
    task_id: str,
    task_updates: TaskUpdateSchema,
    background_tasks: BackgroundTasks,
    current_user: dict = Depends(get_current_user)
):
    task = db.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
        
    # Restrict write access to task owner only
    if task["owner"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not authorized to modify this task.")
        
    updated = db.update_task(task_id, task_updates.model_dump(exclude_none=True))
    
    # Add background update email trigger
    background_tasks.add_task(
        send_task_email_notification,
        current_user["email"],
        current_user["username"],
        updated["title"],
        "update"
    )
    
    return updated

@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(task_id: str, current_user: dict = Depends(get_current_user)):
    task = db.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
        
    if task["owner"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task.")
        
    db.delete_task(task_id)
    return {"message": "Task successfully deleted."}
