# =====================================================================
# TOPIC 1: PYTHON BASICS & DATA TYPES
# =====================================================================
# Is file me hum Python ke variables, basic operators, aur built-in 
# data types ke baare me seekhenge.

# ---------------------------------------------------------------------
# 1. Variables aur Dynamic Typing
# ---------------------------------------------------------------------
# Python dynamically typed hai, yaani aapko data type declare nahi karna padta.
x = 10         # Integer (int)
y = 3.14       # Float
name = "Alice" # String (str)
is_active = True # Boolean (bool)

print("--- 1. Variables & Types ---")
print(f"x is of type: {type(x)}")
print(f"y is of type: {type(y)}")
print(f"name is of type: {type(name)}")
print(f"is_active is of type: {type(is_active)}\n")


# ---------------------------------------------------------------------
# 2. String Manipulation
# ---------------------------------------------------------------------
# Strings in Python are immutable (change nahi ho sakti).
first = "AI"
second = "Automation"
full_name = first + " " + second # Concatenation
print("--- 2. Strings ---")
print(f"Concatenated: {full_name}")
print(f"Uppercase: {full_name.upper()}")
print(f"Length: {len(full_name)}")
# Slicing: [start:stop:step]
print(f"Slicing (first 2 chars): {full_name[:2]}")
print(f"Slicing (reverse string): {full_name[::-1]}\n")


# ---------------------------------------------------------------------
# 3. Lists (Mutable, Ordered Sequence)
# ---------------------------------------------------------------------
# Lists dynamic arrays hoti hain. Inhe create karne ke baad modify kiya ja sakta hai.
tools = ["Python", "FastAPI", "LangChain"]
print("--- 3. Lists ---")
tools.append("LangGraph") # Add at the end
print(f"Added LangGraph: {tools}")
tools[1] = "FastAPI Advanced" # Modifying an element
print(f"Modified: {tools}")
print(f"Pop last element: {tools.pop()}") # Removes and returns last item
print(f"List after pop: {tools}\n")


# ---------------------------------------------------------------------
# 4. Tuples (Immutable, Ordered Sequence)
# ---------------------------------------------------------------------
# Tuples fast hoti hain aur modify nahi ho sakti. API responses or config me use hoti hain.
coordinates = (12.9716, 77.5946) # (Latitude, Longitude)
print("--- 4. Tuples ---")
print(f"Lat: {coordinates[0]}, Long: {coordinates[1]}")
# coordinates[0] = 13.0  # Ye error dega kyunki tuple immutable hai.
print(f"Type: {type(coordinates)}\n")


# ---------------------------------------------------------------------
# 5. Dictionaries (Key-Value Pairs, Unordered/Ordered-by-insertion)
# ---------------------------------------------------------------------
# API responses aur JSON data handle karne ke liye bohot zaroori hai.
agent_config = {
    "model": "gpt-4o",
    "temperature": 0.7,
    "max_tokens": 1000
}
print("--- 5. Dictionaries ---")
print(f"Model used: {agent_config['model']}")
# Naya key-value add ya modify karna:
agent_config["temperature"] = 0.5
agent_config["top_p"] = 0.9
print(f"Updated config: {agent_config}")
# Safe retrieval using .get() to avoid KeyError if key doesn't exist:
print(f"Safety check: {agent_config.get('non_existent_key', 'Default Value')}\n")


# ---------------------------------------------------------------------
# 6. Sets (Unique, Unordered Collection)
# ---------------------------------------------------------------------
# Duplicate items hatane aur membership testing (in operator) ke liye fastest hai.
unique_users = {"user1", "user2", "user3", "user1"} # Duplicate 'user1' will be ignored
print("--- 6. Sets ---")
print(f"Unique Users: {unique_users}")
print(f"Is 'user2' present? {'user2' in unique_users}\n")
# Set Operations (Union, Intersection)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Intersection: {set_a.intersection(set_b)}")
print(f"Union: {set_a.union(set_b)}\n")


# ---------------------------------------------------------------------
# 7. Mutability vs Immutability Concept
# ---------------------------------------------------------------------
# Python me object reference pass hota hai.
# Mutable (List, Dict, Set) change ho sakte hain in-place.
# Immutable (Int, Float, Str, Tuple) naya object create karte hain.
print("--- 7. Mutability Concept ---")
a = [1, 2, 3]
b = a
b.append(4)
print(f"a: {a} (A bhi change ho gaya kyunki list mutable hai!)")
print(f"b: {b}")
