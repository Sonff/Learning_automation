# =====================================================================
# FASTAPI MODULE 2: PYDANTIC SCHEMAS & DATA VALIDATION
# =====================================================================
# Pydantic data validation aur settings management library hai. 
# AI output structured parsing (Structured Output from LLMs) aur secure API 
# request incoming data validations me Pydantic core concept hai.
#
# RUNNING INSTRUCTIONS:
# Terminal: `uvicorn 02_pydantic_schemas:app --reload`
# Docs: http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List, Optional

app = FastAPI(
    title="FastAPI Learning - Module 2",
    description="Pydantic V2 schemas and advanced data validation",
)

# ---------------------------------------------------------------------
# 1. Nesting Models & Field Constraints
# ---------------------------------------------------------------------
# Sub-models dynamically structured documents build karne me use hote hain.

class Tag(BaseModel):
    name: str = Field(..., min_length=2, max_length=20) # '...' represents required field
    category: str = Field("general")

class BlogInput(BaseModel):
    title: str = Field(..., min_length=5, max_length=100, description="Blog post ka title")
    content: str = Field(..., description="Post body content")
    # EmailStr (pydantic[email] integration) ensure karta hai correct email syntax:
    author_email: EmailStr 
    # Field numerical validations:
    rating: Optional[int] = Field(default=5, ge=1, le=5) # ge=Greater/Equal, le=Less/Equal
    # Nested Model: List of Tag objects
    tags: List[Tag] = Field(default=[])

    # -----------------------------------------------------------------
    # 2. Custom Validator (Field Validation Logic)
    # -----------------------------------------------------------------
    @field_validator("title")
    @classmethod
    def prevent_clickbait(cls, value: str) -> str:
        # Custom logic to check check titles strings
        clickbait_words = ["buzzfeed", "click here", "shocking", "must see"]
        for word in clickbait_words:
            if word in value.lower():
                raise ValueError(f"Title contains clickbait word: '{word}'. This is blocked.")
        return value


# ---------------------------------------------------------------------
# 3. Validation Testing Endpoint
# ---------------------------------------------------------------------
@app.post("/blogs")
async def create_blog(blog: BlogInput):
    # Validation fail hone par FastAPI automatic client ko detailed error list
    # return karta hai without executing this function body.
    
    # model_dump() python dict extraction ke liye use hota hai.
    blog_data = blog.model_dump()
    
    return {
        "status": "validated",
        "post_details": blog_data,
        "total_tags": len(blog.tags)
    }

# ---------------------------------------------------------------------
# 4. JSON Serialization / Parsing Manual (LLM output simulation)
# ---------------------------------------------------------------------
# Kai baar humein direct raw string ko validate karke model parse karna hota hai.
# (Jaise LLM JSON string response output create kare).

@app.post("/parse-llm-response")
async def parse_response(raw_json: str):
    try:
        # Raw string ko direct model input structure parse karne ka tareeka:
        parsed_blog = BlogInput.model_validate_json(raw_json)
        return {
            "parse_status": "success",
            "data": parsed_blog.model_dump()
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to parse LLM JSON: {str(e)}"
        )
