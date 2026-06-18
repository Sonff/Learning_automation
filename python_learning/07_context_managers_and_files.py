# =====================================================================
# TOPIC 7: CONTEXT MANAGERS & FILE/JSON OPERATIONS
# =====================================================================
# File operations aur environment config JSON load karne ke liye 
# Safe Resource management (Context Managers) extremely critical hai to 
# avoid memory leaks or database lock errors.

import json
from contextlib import contextmanager

# ---------------------------------------------------------------------
# 1. Standard File I/O and JSON handling
# ---------------------------------------------------------------------
# `with` keyword ensure karta hai ki operations perform hone ke baad 
# file auto-close ho jaye (even if errors occur).

config_data = {
    "api_version": "v2",
    "debug": True,
    "max_retries": 5
}

print("--- 1. File Handling & JSON Write/Read ---")
# JSON File writing
with open("test_config.json", "w") as file:
    json.dump(config_data, file, indent=4) # python dict written as formatted JSON string
print("test_config.json written successfully.")

# JSON File reading
with open("test_config.json", "r") as file:
    loaded_data = json.load(file)
print(f"Loaded JSON: {loaded_data}")
print(f"debug status: {loaded_data['debug']}")
print()


# ---------------------------------------------------------------------
# 2. Custom Class-based Context Manager (__enter__, __exit__)
# ---------------------------------------------------------------------
# Custom actions jaise connecting database, starting transactions, or 
# locking resources.

class DatabaseConnector:
    def __init__(self, db_name: str):
        self.db_name = db_name
        
    def __enter__(self):
        print(f"[DB] Connecting to database '{self.db_name}'...")
        # Database connection mock-up
        return self # Object block ke andar as a variable available hota hai
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # clean-up logic (har haal me execute hoga)
        print(f"[DB] Closing connection to database '{self.db_name}'.")
        if exc_type:
            print(f"[DB] Error caught during execution: {exc_val}")
        return True # True returns suppression of exceptions. False crashes script if error occurred inside.

print("--- 2. Class Context Manager ---")
with DatabaseConnector("user_profile_db") as db:
    print(f"Using DB reference to load profiles...")
    # Raising an error to check safe release
    # raise ValueError("DB query syntax error!")
print("Outside Context block - status check: Done.\n")


# ---------------------------------------------------------------------
# 3. Custom Function-based Context Manager (@contextmanager decorator)
# ---------------------------------------------------------------------
# Simple flows ke liye class banana zaroori nahi, contextlib decorator use karein.

@contextmanager
def file_logger(filepath: str):
    print(f"[Logger] Opening log file: {filepath}")
    log_file = open(filepath, "a")
    try:
        yield log_file # Is target block block variables ko execute hone deta hai
    finally:
        # yield completed or any error caught then execute finally block
        print(f"[Logger] Auto-closing log file: {filepath}")
        log_file.close()

print("--- 3. Generator Context Manager ---")
with file_logger("execution.log") as logger:
    logger.write("Automation pipeline run successful.\n")
    logger.write("Status: OK.\n")
print("Log updates complete.")
print()
