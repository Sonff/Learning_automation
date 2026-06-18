# =====================================================================
# TOPIC 8: ASYNCHRONOUS PROGRAMMING (ASYNCIO)
# =====================================================================
# FastAPI aur AI Agents (LangGraph) multi-tasking and parallel API calls 
# (LLM calls) handle karne ke liye async/await use karte hain. 
# Agar synchronous code likhoge toh user requests wait queues me freeze ho jayengi.

import asyncio
import time

# ---------------------------------------------------------------------
# 1. Understanding async/await and Co-routines
# ---------------------------------------------------------------------
# `async def` function ek coroutine return karta hai. Direct call karne par 
# code execute nahi hota, execute karne ke liye `await` karna padta hai.

async def fetch_api_status():
    print("API status fetch starting...")
    # asyncio.sleep() event loop ko block nahi karta, other tasks run ho sakte hain.
    # time.sleep() poore python thread ko freeze/block kar deta hai.
    await asyncio.sleep(1.0)
    print("API status fetch complete!")
    return {"status": "operational"}


# ---------------------------------------------------------------------
# 2. Concurrency with asyncio.gather (Parallel Execution)
# ---------------------------------------------------------------------
# Maan lijiye aapko 3 LLM models ko parallelly call karna hai:

async def call_llm(model_name: str, delay: float):
    print(f"[{model_name}] Querying model...")
    await asyncio.sleep(delay) # Simulation of network API lag
    print(f"[{model_name}] Response received!")
    return f"Response from {model_name}"

async def run_parallel_llms():
    print("--- 2. Parallel Tasks using asyncio.gather ---")
    start = time.time()
    
    # 3 APIs calls ko register karke event loop ko submit karna:
    task1 = call_llm("gpt-4o", 1.5)
    task2 = call_llm("claude-3-5", 2.0)
    task3 = call_llm("gemini-1.5", 1.0)
    
    # asyncio.gather concurrently run karega sabko ek sath:
    responses = await asyncio.gather(task1, task2, task3)
    
    end = time.time()
    print(f"All Responses: {responses}")
    # Total time lagbhag max delay (2.0s) ke aas paas hoga, na ki sum of delays (4.5s)
    print(f"Time taken concurrently: {end - start:.2f} seconds\n")


# ---------------------------------------------------------------------
# 3. Running Async main function
# ---------------------------------------------------------------------
# Async flow initialize karne ke liye hum standard main run configuration use karte hain.

async def main():
    print("--- 1. Simple Coroutine Execution ---")
    # Await simple coroutine
    result = await fetch_api_status()
    print(f"Result: {result}\n")
    
    # Run concurrent tasks
    await run_parallel_llms()

if __name__ == "__main__":
    # Event loop run karne ke liye standard launcher:
    asyncio.run(main())
