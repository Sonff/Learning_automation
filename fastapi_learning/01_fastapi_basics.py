# =====================================================================
# FASTAPI MODULE 1: BASICS & ROUTING
# =====================================================================
# Is file me hum FastAPI ke basic routing, path parameters, query parameters
# aur client se simple data receive karne ka tareeka seekhenge.
#
# RUNNING INSTRUCTIONS:
# Terminal me run karein: `uvicorn 01_fastapi_basics:app --reload`
# Aur browser me open karein: http://127.0.0.1:8000
# Docs check karne ke liye: http://127.0.0.1:8000/docs (Swagger UI)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# FastAPI app initialize karna
app = FastAPI(
    title="FastAPI Learning - Module 1",
    description="Basics of routing, params, and body in FastAPI",
    version="1.0"
)

# ---------------------------------------------------------------------
# 1. Root Endpoint (GET Request)
# ---------------------------------------------------------------------
# GET request read ya retrieval actions ke liye use hoti hai.
@app.get("/")
async def read_root():
    return {
        "message": "Welcome to Phase 2: FastAPI and API Design!",
        "status": "active",
        "docs_url": "http://127.0.0.1:8000/docs"
    }


# ---------------------------------------------------------------------
# 2. Path Parameters (GET Request with dynamic path)
# ---------------------------------------------------------------------
# Path parameters URL ka part hote hain, jaise /items/101.
# Type hinting (: int) ensure karta hai ki dynamic parameter correct format me ho.
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    # Agar path parameters me alpha input ('abc') diya toh FastAPI client ko automatic
    # 422 Unprocessable Entity error validation return karega.
    return {
        "item_id": item_id,
        "location": "Path Parameter",
        "status": "verified"
    }


# ---------------------------------------------------------------------
# 3. Query Parameters (GET Request with filters)
# ---------------------------------------------------------------------
# Query parameters URL me `?` ke baad aate hain, jaise /search?q=python&limit=10.
# Inhe variables parameters declare kiya jata hai jo route structure ka part nahi hote.
@app.get("/search")
async def search_items(q: str, limit: int = 10, offset: Optional[int] = 0):
    # 'limit' default argument 10 hai. 'offset' optional parameter hai.
    return {
        "search_query": q,
        "limit": limit,
        "offset": offset,
        "results": [f"Result item {i}" for i in range(offset, offset + limit)]
    }


# ---------------------------------------------------------------------
# 4. Request Body (POST Request)
# ---------------------------------------------------------------------
# POST request data create/submit karne ke liye use hoti hai.
# Client payload receive karne ke liye hum Pydantic dynamic models define karte hain.

class UserCreate(BaseModel):
    username: str
    email: str
    age: int
    is_active: Optional[bool] = True # Default True value if not provided

@app.post("/users")
async def create_user(user: UserCreate):
    # 'user' object automatic validate hokar Pydantic model me wrap ho jayega.
    # Aap is data ko dict me convert kar sakte hain standard database transactions ke liye:
    user_dict = user.model_dump() # Pydantic v2 syntax (v1 was user.dict())
    
    return {
        "message": "User validation successful!",
        "received_data": user_dict,
        "processed_username": user.username.upper()
    }
