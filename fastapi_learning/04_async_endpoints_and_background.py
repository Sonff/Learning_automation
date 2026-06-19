# =====================================================================
# FASTAPI MODULE 4: ASYNC ENDPOINTS & BACKGROUND TASKS
# =====================================================================
# AI Agent workflows me LLM generation ya reports compilation time leti hai.
# Agar hum client ko line pe wait karwaenge toh API timeout errors aenge.
# Solution: BackgroundTasks. User ko turant response de do (e.g. "Processing started"),
# aur task ko system background thread me run hone do.
#
# RUNNING INSTRUCTIONS:
# Terminal: `uvicorn 04_async_endpoints_and_background:app --reload`
# Docs: http://127.0.0.1:8000/docs

from fastapi import FastAPI, BackgroundTasks, HTTPException
import asyncio
import time

app = FastAPI(
    title="FastAPI Learning - Module 4",
    description="Asynchronous endpoints and BackgroundTasks configuration",
)

# Mock logger / Database variable for background task updates
task_logs = {}

# ---------------------------------------------------------------------
# 1. Background Task Worker Function
# ---------------------------------------------------------------------
# Yeh normal function (def) ya async function (async def) ho sakta hai.
# Isme CPU-heavy tasks ya long API requests run karte hain.
async def process_llm_report_background(task_id: str, prompt: str):
    print(f"[Worker] Task {task_id} initialized in background...")
    task_logs[task_id] = "Processing - Running prompt in LLM engine"
    
    # Simulating long-running LLM generation (e.g., 5 seconds)
    await asyncio.sleep(5.0)
    
    # Process complete updates
    print(f"[Worker] Task {task_id} generation complete.")
    task_logs[task_id] = f"Completed - Summary report for prompt: '{prompt}' successfully generated."


# ---------------------------------------------------------------------
# 2. Async Endpoints (Using await)
# ---------------------------------------------------------------------
# FastAPI single thread par hazaro parallel requests handle karta hai
# if they are asynchronous (non-blocking).
@app.post("/trigger-report-direct")
async def generate_report_direct(prompt: str):
    # Direct flow block:
    # User ko 3 seconds wait karna padega response milne se pehle.
    start = time.time()
    await asyncio.sleep(3.0) # non-blocking network wait
    end = time.time()
    
    return {
        "status": "success",
        "time_taken_seconds": round(end - start, 2),
        "data": f"Report content for: {prompt}"
    }


# ---------------------------------------------------------------------
# 3. Background Task Endpoint
# ---------------------------------------------------------------------
# FastAPI `BackgroundTasks` parameters provide karta hai. Naye tasks ko 
# `add_task` karke queue me add kiya jata hai aur immediate response return hota hai.

@app.post("/trigger-report-background")
async def generate_report_background(
    prompt: str, 
    background_tasks: BackgroundTasks # FastAPI will inject this automatically
):
    # Dynamic task ID create karna
    task_id = f"task_{int(time.time())}"
    task_logs[task_id] = "Queued"
    
    # Background task queue me worker function configure karna:
    # Format: background_tasks.add_task(function_name, *arguments_for_function)
    background_tasks.add_task(process_llm_report_background, task_id, prompt)
    
    # Immediate response return hoga (no waiting!):
    return {
        "message": "Report generation started in background.",
        "task_id": task_id,
        "status_check_url": f"http://127.0.0.1:8000/task-status/{task_id}"
    }


# ---------------------------------------------------------------------
# 4. Status Check Endpoint
# ---------------------------------------------------------------------
@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    status_info = task_logs.get(task_id)
    if not status_info:
        raise HTTPException(status_code=404, detail="Task ID not found.")
        
    return {
        "task_id": task_id,
        "status": status_info
    }
