# =====================================================================
# TOPIC 6: DECORATORS & GENERATORS
# =====================================================================
# Decorators: APIs logging, execution time measure karne, auth verify 
# karne ke liye use hote hain.
# Generators: Large text/datasets process karte waqt system memory usage 
# minimal rakhne ke liye useful hote hain.

import time

# ---------------------------------------------------------------------
# 1. Understanding Closures (Nested Functions)
# ---------------------------------------------------------------------
# Outer function state memory me save rakhti hai even after execution completion.
def multiplier(factor: int):
    def multiply(number: int) -> int:
        return number * factor
    return multiply

print("--- 1. Closures ---")
double = multiplier(2) # 'factor' 2 set ho gaya closure state me
triple = multiplier(3)
print(f"Double of 10: {double(10)}")
print(f"Triple of 10: {triple(10)}\n")


# ---------------------------------------------------------------------
# 2. Decorators (Modify function behavior without changing code)
# ---------------------------------------------------------------------
# Decorator ek function leta hai, wrap karta hai, behavior modify karke 
# modified function return karta hai.

# Decorator definition
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) # Actual function execute hota hai
        end_time = time.time()
        print(f"[Timer] Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# Applying decorator using '@'
@timer_decorator
def fetch_llm_response(prompt: str):
    print(f"Sending prompt to LLM: '{prompt}'")
    time.sleep(1.5) # Simulating API latency delay
    return "This is the generated AI response."

print("--- 2. Decorators ---")
response = fetch_llm_response("What is RAG?")
print(f"Result: {response}\n")


# ---------------------------------------------------------------------
# 3. Generators (`yield` keyword)
# ---------------------------------------------------------------------
# Normal function data return karne ke baad complete return ho jata hai,
# memory release ho jati hai.
# Generator dynamic generator object return karta hai aur state 'yield' par 
# pause kar deta hai. Jab tak request na ho tab tak next value evaluate nahi karta.

def read_huge_file():
    # Poori file memory load karne ke bajaye chunk by chunk read karein:
    print("Reading first chunk...")
    yield "Chunk 1: Initial document metadata."
    
    print("Reading second chunk...")
    yield "Chunk 2: Main body text."
    
    print("Reading final chunk...")
    yield "Chunk 3: Reference footnotes."

print("--- 3. Generators ---")
gen = read_huge_file()
print(f"Generator Object: {gen}")

# Calling next() outputs data until yield
print(next(gen))
print("-" * 15)
print(next(gen))
print("-" * 15)
print(next(gen))

# Iterating over a generator (Standard usage in loops)
print("\nIterating with for-loop (Fresh generator):")
for chunk in read_huge_file():
    print(f"Received: {chunk}")
print()
