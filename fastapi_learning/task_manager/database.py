# =====================================================================
# TASK MANAGER PROJECT: DATABASE (database.py)
# =====================================================================
# Real database setup (SQLAlchemy/PostgreSQL) seekhne se pehle learning 
# ke liye ek robust, thread-safe in-memory mock database implementation.

from typing import Dict, Any, List, Optional
import threading

class MockDB:
    def __init__(self):
        # Thread safety locks taaki parallel requests data corruption na karein
        self.lock = threading.Lock()
        self.users: Dict[str, Dict[str, Any]] = {} # username -> user_data_dict
        self.tasks: Dict[str, Dict[str, Any]] = {} # task_id -> task_data_dict
        self.task_counter = 0

    # -----------------------------------------------------------------
    # User DB Actions
    # -----------------------------------------------------------------
    def get_user(self, username: str) -> Optional[Dict[str, Any]]:
        with self.lock:
            return self.users.get(username.lower())

    def save_user(self, user_data: Dict[str, Any]):
        with self.lock:
            username = user_data["username"].lower()
            self.users[username] = user_data

    # -----------------------------------------------------------------
    # Task DB Actions
    # -----------------------------------------------------------------
    def create_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        with self.lock:
            self.task_counter += 1
            task_id = f"task_{self.task_counter}"
            task_data["id"] = task_id
            self.tasks[task_id] = task_data
            return task_data

    def get_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        with self.lock:
            return self.tasks.get(task_id)

    def get_user_tasks(self, username: str) -> List[Dict[str, Any]]:
        with self.lock:
            return [
                task for task in self.tasks.values() 
                if task["owner"].lower() == username.lower()
            ]

    def update_task(self, task_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        with self.lock:
            if task_id not in self.tasks:
                return None
            task = self.tasks[task_id]
            for key, val in updates.items():
                if val is not None:
                    task[key] = val
            self.tasks[task_id] = task
            return task

    def delete_task(self, task_id: str) -> bool:
        with self.lock:
            if task_id in self.tasks:
                del self.tasks[task_id]
                return True
            return False

# Database Instance initialize karna (taaki saari files isi instance ko import karein)
db = MockDB()
