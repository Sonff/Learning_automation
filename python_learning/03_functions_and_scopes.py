# =====================================================================
# TOPIC 3: FUNCTIONS, ARGUMENTS, & SCOPES
# =====================================================================
# Is file me hum reusable code components (functions), dynamic arguments
# (args/kwargs), Lambda expressions aur scope management seekhenge.

# ---------------------------------------------------------------------
# 1. Basic Function and Docstrings
# ---------------------------------------------------------------------
# Docstrings functions ke behavior aur types ko specify karne ke kaam aati hain.
def greet_user(name: str, greeting: str = "Hello") -> str:
    """
    User ko greet karne ke liye function.
    
    Args:
        name: Name of the user.
        greeting: Default greeting message.
        
    Returns:
        Formatted greeting string.
    """
    return f"{greeting}, {name}!"

print("--- 1. Function & Type Hints ---")
print(greet_user("Amit"))
print(greet_user("Rahul", greeting="Good Morning"))
# Documentation access karna:
# print(greet_user.__doc__)
print()


# ---------------------------------------------------------------------
# 2. Variable Arguments (*args and **kwargs)
# ---------------------------------------------------------------------
# *args: Positional arguments receive karta hai as a TUPLE.
# **kwargs: Keyword arguments receive karta hai as a DICTIONARY.
# LangChain aur complex libraries me functions standard configuration bypass 
# karne ke liye args/kwargs ka heavily use karti hain.

def execute_task(task_name: str, *args, **kwargs):
    print(f"Executing: {task_name}")
    if args:
        print(f"Extra positional args (tuple): {args}")
    if kwargs:
        print(f"Configuration kwargs (dict): {kwargs}")

print("--- 2. *args and **kwargs ---")
# Call with positional only:
execute_task("Backup Database", "drive_d", "backup_v1.zip")

print("-" * 20)
# Call with keyword args:
execute_task("Generate Report", format="pdf", pages=10, include_images=True)
print()


# ---------------------------------------------------------------------
# 3. Lambda Functions (Anonymous / One-liner)
# ---------------------------------------------------------------------
# Single-line functions jo on-the-fly computational sorting/mapping me use hote hain.
print("--- 3. Lambda Functions ---")
square = lambda x: x * x
print(f"Lambda square of 5: {square(5)}")

# Real world use: Sorting list of dictionaries based on key
users = [
    {"name": "Amit", "age": 30},
    {"name": "Sanjay", "age": 22},
    {"name": "Priya", "age": 25}
]
# Age ke basis par sort karna
users.sort(key=lambda u: u["age"])
print(f"Sorted Users by Age: {users}\n")


# ---------------------------------------------------------------------
# 4. Scopes (Local, Enclosing, Global, Built-in - LEGB Rule)
# ---------------------------------------------------------------------
# Variables ka access boundary.
print("--- 4. Variables Scopes ---")
global_var = "I am Global"

def outer_function():
    enclosing_var = "I am Enclosing (Outer)"
    
    def inner_function():
        local_var = "I am Local"
        print(f"Inner accessing: {local_var}")
        print(f"Inner accessing: {enclosing_var}")
        print(f"Inner accessing: {global_var}")
        
    inner_function()

outer_function()

# Modifying global variable inside a function needs the 'global' keyword:
counter = 0

def increment():
    global counter # Batata hai ki outer variable use karna hai
    counter += 1

increment()
print(f"Global counter after function modify: {counter}\n")
