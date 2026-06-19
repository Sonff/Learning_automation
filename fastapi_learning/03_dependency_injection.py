# =====================================================================
# FASTAPI MODULE 3: DEPENDENCY INJECTION (Depends)
# =====================================================================
# Dependency Injection ka matlab hai "Apne endpoint functions ko variables,
# configurations, resources, ya actions (jaise auth checkout) pre-load karke dena".
#
# FastAPI me iske liye `Depends` use hota hai.
#
# RUNNING INSTRUCTIONS:
# Terminal: `uvicorn 03_dependency_injection:app --reload`
# Docs: http://127.0.0.1:8000/docs

from fastapi import FastAPI, Depends, Header, HTTPException, status
from typing import Dict

app = FastAPI(
    title="FastAPI Learning - Module 3",
    description="Dependency Injection patterns using Depends",
)

# ---------------------------------------------------------------------
# 1. Config Dependency (Mock Loading Application Settings)
# ---------------------------------------------------------------------
# Ek function jo database url, settings compile karke share kare.
def get_app_settings() -> Dict[str, str]:
    return {
        "db_host": "localhost",
        "db_port": "5432",
        "api_key_secret": "my-agentic-secure-token-101"
    }


# ---------------------------------------------------------------------
# 2. Database Connection Dependency (Yield Pattern)
# ---------------------------------------------------------------------
# Resource management (opening/closing connections) automatically handle karne ke liye 
# yield generator pattern use hota hai.
def get_db_connection():
    print("[DB] ---> Opening Database Session Connection pool...")
    db_session = {"connection_id": "session_9921", "status": "active"}
    try:
        yield db_session  # Endpoint ko db session provide karega
    finally:
        # Await endpoint execution completion, then run cleanup:
        print("[DB] <--- Closing Database Session Connection pool safely.\n")


# ---------------------------------------------------------------------
# 3. Security / Auth Dependency
# ---------------------------------------------------------------------
# Har incoming request me header variables check karne aur parse karne ke liye.
def verify_api_key(
    x_api_key: str = Header(..., description="API Access key verification header"),
    settings: dict = Depends(get_app_settings) # Dependency inside dependency!
):
    expected_key = settings["api_key_secret"]
    if x_api_key != expected_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key in headers."
        )
    return {"user": "authorized_bot", "permissions": "write_access"}


# ---------------------------------------------------------------------
# 4. Endpoints Utilizing Dependencies
# ---------------------------------------------------------------------
# A. Reading system settings (simple Depends)
@app.get("/system-info")
async def get_system_info(config: dict = Depends(get_app_settings)):
    return {
        "system_status": "OK",
        "db_host_active": config["db_host"]
    }

# B. Performing DB Operations (Uses get_db_connection generator dependency)
@app.get("/items")
async def read_items(db = Depends(get_db_connection)):
    # Endpoint call hone par:
    # 1. get_db_connection run hoga up to `yield`.
    # 2. read_items executes containing database logic.
    # 3. Finally block of get_db_connection executes.
    return {
        "data": ["itemA", "itemB"],
        "session_used": db["connection_id"]
    }

# C. Secure endpoint requiring API Key Verification
# verify_api_key runs and outputs return value to 'auth_payload' variable
@app.get("/secure-data")
async def read_secure_details(
    auth_payload: dict = Depends(verify_api_key),
    db = Depends(get_db_connection)
):
    return {
        "message": "Access granted to secure portal",
        "auth_details": auth_payload,
        "db_session_id": db["connection_id"]
    }
