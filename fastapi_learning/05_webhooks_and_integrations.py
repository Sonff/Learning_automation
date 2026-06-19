# =====================================================================
# FASTAPI MODULE 5: WEBHOOKS & THIRD-PARTY INTEGRATIONS
# =====================================================================
# Real-world automation systems me webhooks aur third-party APIs (jaise 
# Slack notifications, LLM providers APIs) call karna dynamic skill hai.
#
# Is module me hum HTTPX library use karke ASYNC outgoing HTTP calls karna,
# aur incoming Webhooks receive karna seekhenge.
#
# RUNNING INSTRUCTIONS:
# Terminal: `uvicorn 05_webhooks_and_integrations:app --reload`
# Docs: http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import httpx
from typing import Dict, Any, Optional

app = FastAPI(
    title="FastAPI Learning - Module 5",
    description="Handling incoming webhooks & executing outgoing async API requests using HTTPX",
)

# ---------------------------------------------------------------------
# 1. Incoming Webhook Receiver Endpoint
# ---------------------------------------------------------------------
# Webhooks simply standard POST requests hoti hain jo koi external service 
# (jaise Stripe, GitHub) aapke endpoint par data send karne ke liye call karti hai.

class GitHubWebhookPayload(BaseModel):
    repository: str
    sender: str
    action: str
    commit_message: Optional[str] = None

@app.post("/webhooks/github")
async def github_webhook_receiver(payload: GitHubWebhookPayload):
    # Dynamic processing of the incoming webhook payload
    print(f"[Webhook Recieved] Repo: {payload.repository} | Action: {payload.action}")
    print(f"Triggered by: {payload.sender}")
    
    # Process actions based on incoming event:
    if payload.action == "push":
        # Yahan hum pipeline trigger, email sending ya state change configure kar sakte hain
        print(f"Analyzing commit: '{payload.commit_message}' for security checks...")
        
    return {"status": "event_processed", "action_registered": payload.action}


# ---------------------------------------------------------------------
# 2. Outgoing Asynchronous API Integration (Using httpx.AsyncClient)
# ---------------------------------------------------------------------
# FastAPI applications me synchronous `requests` library use nahi karni chahiye
# kyunki woh blocking hoti hai. Use `httpx` (async client) instead.

# Mock External service URL (e.g. JSONPlaceholder to test api calls)
MOCK_API_URL = "https://jsonplaceholder.typicode.com/posts"

@app.get("/fetch-external-post/{post_id}")
async def fetch_external_post(post_id: int):
    # httpx.AsyncClient as a context manager use karein connection pool reuse ke liye
    async with httpx.AsyncClient() as client:
        try:
            # Non-blocking async GET request to external server
            response = await client.get(f"{MOCK_API_URL}/{post_id}", timeout=5.0)
            
            # Response check
            if response.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"External post with ID {post_id} not found."
                )
            
            # Raise exception for 5xx errors automatically
            response.raise_for_status()
            
            data = response.json()
            return {
                "integration_source": "jsonplaceholder_mock_api",
                "extracted_data": data
            }
            
        except httpx.RequestError as exc:
            # Handling connection exceptions
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Failed to communicate with external API: {str(exc)}"
            )


# ---------------------------------------------------------------------
# 3. Outgoing Post API Call (Simulating Sending Slack Message)
# ---------------------------------------------------------------------
class SlackMessageSchema(BaseModel):
    channel: str
    message: str

@app.post("/send-slack-alert")
async def send_slack_alert(payload: SlackMessageSchema):
    slack_webhook_payload = {
        "channel": payload.channel,
        "text": f"🚨 [System Alert]: {payload.message}"
    }
    
    # Simulation: Actual webhook post:
    # async with httpx.AsyncClient() as client:
    #     response = await client.post("https://hooks.slack.com/services/...", json=slack_webhook_payload)
    
    return {
        "status": "mock_sent",
        "channel_target": payload.channel,
        "sent_payload": slack_webhook_payload
    }
