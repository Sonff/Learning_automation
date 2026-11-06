"""
Module 13: String & List Operations and Comprehensions
Useful for data processing, text parsing, and everyday automation.
"""

def string_manipulation_examples():
    text = "  learning automation and ai agents with python  "
    print("--- String Operations ---")
    print(f"Original: '{text}'")
    
    # Cleaning whitespace and case formatting
    cleaned = text.strip().title()
    print(f"Cleaned & Title Case: '{cleaned}'")
    
    # Splitting and joining
    words = cleaned.split()
    joined_kebab = "-".join(words).lower()
    print(f"Kebab Case: {joined_kebab}")
    
    # Checking prefix / suffix
    filename = "report_2026_11_06.csv"
    if filename.endswith(".csv"):
        print(f"'{filename}' is a CSV data file.")


def list_comprehension_examples():
    print("\n--- List Comprehension & Filtering ---")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Squares of even numbers
    even_squares = [n ** 2 for n in numbers if n % 2 == 0]
    print(f"Even Squares: {even_squares}")
    
    # Categorize numbers
    categories = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
    print(f"Odd/Even Mapping: {dict(zip(numbers, categories))}")


def automation_task_example():
    print("\n--- Practical Automation Data Parsing ---")
    raw_logs = [
        "2026-11-06 10:00:00 - INFO - Task started",
        "2026-11-06 10:05:22 - ERROR - Connection timed out",
        "2026-11-06 10:06:15 - WARNING - High memory usage",
        "2026-11-06 10:10:00 - INFO - Task finished successfully",
    ]
    
    # Extract only error and warning logs
    alerts = [log for log in raw_logs if "ERROR" in log or "WARNING" in log]
    print(f"Found {len(alerts)} alerts:")
    for alert in alerts:
        print(f"  -> {alert}")


if __name__ == "__main__":
    string_manipulation_examples()
    list_comprehension_examples()
    automation_task_example()
