# =====================================================================
# TOPIC 2: CONTROL FLOW & LOOPS
# =====================================================================
# Is file me hum conditionals (if-else), loops, and comprehensions ke 
# baare me seekhenge jo workflow automation me logic setup karne ke kaam aate hain.

# ---------------------------------------------------------------------
# 1. Conditionals (if, elif, else)
# ---------------------------------------------------------------------
print("--- 1. Conditionals ---")
status_code = 404

if status_code == 200:
    print("Success: Request was successful!")
elif status_code == 404:
    print("Error: Resource not found!")
elif status_code == 500:
    print("Error: Internal Server Error!")
else:
    print("Unknown status code.")

# Logical Operators: and, or, not
authorized = True
has_permission = False

if authorized and not has_permission:
    print("User is logged in but does not have execution permission.")
print()


# ---------------------------------------------------------------------
# 2. Loops (for, while)
# ---------------------------------------------------------------------
print("--- 2. Loops ---")
# For loop mostly sequences pe iterate karne ke liye use hota hai.
print("Iterating a list of agents:")
agents = ["Router", "Researcher", "Writer"]
for agent in agents:
    print(f" - Running Agent: {agent}")

# Using range(start, stop, step)
print("\nCounting using range:")
for i in range(1, 4):  # 1, 2, 3 (stop is exclusive)
    print(f"Count: {i}")

# While loop check condition until it becomes False
print("\nWhile loop countdown:")
counter = 3
while counter > 0:
    print(f"Retrying API connection... (Attempts left: {counter})")
    counter -= 1
print()


# ---------------------------------------------------------------------
# 3. Loop Control Statements (break, continue, else)
# ---------------------------------------------------------------------
print("--- 3. Break, Continue & Else ---")
# 'break' loop se exit kar deta hai.
# 'continue' current iteration skip karke next loop start karta hai.
print("Break & Continue Demo:")
for num in range(1, 6):
    if num == 3:
        print("Skipping 3 (continue)")
        continue
    if num == 5:
        print("Breaking loop at 5 (break)")
        break
    print(f"Number: {num}")

# Loop Else: For loop ke end me else tab chalta hai jab loop bina 'break' ke 
# complete ho jaye. Useful for search success checking.
print("\nFor-Else Demo:")
for x in [1, 2, 3]:
    print(f"Checking item {x}")
else:
    print("Loop finished naturally without break!")
print()


# ---------------------------------------------------------------------
# 4. List and Dictionary Comprehensions
# ---------------------------------------------------------------------
# Pythonic, concise tarika loops aur lists/dicts ko build karne ka.
print("--- 4. Comprehensions ---")

# Normal way:
# square_numbers = []
# for i in range(5):
#     square_numbers.append(i * i)

# Comprehension way:
square_numbers = [i * i for i in range(5)]
print(f"List Comprehension: {square_numbers}")

# Comprehension with condition (if):
even_squares = [i * i for i in range(10) if i % 2 == 0]
print(f"Even Squares (Filtered): {even_squares}")

# Dictionary Comprehension:
# Dynamic configuration mappings ya status dictionary create karne me useful hai.
agent_names = ["researcher_agent", "reviewer_agent"]
agent_status = {name: "idle" for name in agent_names}
print(f"Dict Comprehension: {agent_status}")
print()
