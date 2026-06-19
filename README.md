# 🚀 Learning Automation & AI Agents

Welcome to my learning journey of building **AI-powered Automations and Intelligent Agents**! This repository is designed to track my progress from Python fundamentals to advanced, production-grade AI applications.

---

## 🗺️ Learning Roadmap Progress

Here is my step-by-step developer roadmap. As I complete each phase, I will add the code and update the checkmarks below.

- [x] **Phase 1: Python Core & Advanced** (Variables, OOPs, Generators, Asyncio Concurrency)
- [x] **Phase 2: FastAPI & API Design** (Backend structures, dependency injection, webhooks)
- [ ] **Phase 3: LLM Foundations & Tool Calling** (Prompt engineering, structured JSON output, function calling)
- [ ] **Phase 4: Vector Databases & RAG** (ChromaDB/Qdrant, document chunking, hybrid search)
- [ ] **Phase 5: LangGraph & Stateful AI Agents** (Nodes, edges, states, human-in-the-loop, multi-agent systems)
- [ ] **Phase 6: Advanced Automation** (Browser automation with Playwright, task queues with Celery & Redis)
- [ ] **Phase 7: Production Deployment & LLMOps** (Dockerization, Cloud hosting, tracing with LangSmith)

---

## 📂 Repository Structure

### 🐍 Phase 1: Python Learning Modules (`/python_learning`)

This folder contains modular scripts with detailed explanations (in Hinglish & English) covering everything needed to write robust backend code and AI pipelines.

| Module File | Topic Covered | Key Concepts |
| :--- | :--- | :--- |
| 📄 [01_basics_and_data_types.py](./python_learning/01_basics_and_data_types.py) | Python Basics | Variables, Strings, Lists, Tuples, Dictionaries, Sets, Mutability |
| 📄 [02_control_flow_and_loops.py](./python_learning/02_control_flow_and_loops.py) | Control Flow | If-elif-else, For/While Loops, Loop Else, Comprehensions |
| 📄 [03_functions_and_scopes.py](./python_learning/03_functions_and_scopes.py) | Functions | Docstrings, Type Hints, `*args` & `**kwargs`, Lambda, Variable Scopes (LEGB) |
| 📄 [04_oop_fundamentals.py](./python_learning/04_oop_fundamentals.py) | OOP Basics | Classes, Objects, Constructors (`__init__`), Instance vs Class attributes |
| 📄 [05_oop_advanced.py](./python_learning/05_oop_advanced.py) | Advanced OOP | Inheritance (`super()`), Encapsulation, `@property` decorators, Dunder/Magic methods |
| 📄 [06_decorators_and_generators.py](./python_learning/06_decorators_and_generators.py) | Functional Python | Closures, Custom Decorators (wrapper functions), Generators (`yield` memory optimizations) |
| 📄 [07_context_managers_and_files.py](./python_learning/07_context_managers_and_files.py) | Resource Management | File I/O, JSON processing, Custom class/function-based Context Managers (`with`) |
| 📄 [08_asyncio_concurrency.py](./python_learning/08_asyncio_concurrency.py) | Async Python | Coroutines (`async`/`await`), Event loops, Non-blocking delays, `asyncio.gather` for parallel APIs |
| 📄 [09_leetcode_python_tricks.py](./python_learning/09_leetcode_python_tricks.py) | Competitive & DSA | Class solutions, Collections (`deque`, `Counter`, `defaultdict`), `heapq` Heaps, `bisect` |
| 📄 [10_robotics_ai_school_fundamentals.py](./python_learning/10_robotics_ai_school_fundamentals.py) | Teaching / Kids Guide | Basics explained via Robots/Sensors, Interactive Smart Vacuum Cleaner Simulator game |

### ⚡ Phase 2: FastAPI & API Design (`/fastapi_learning`)

This folder contains step-by-step FastAPI endpoints, validation mechanisms, webhooks, and the core Task Management project.

| Module File / Folder | Topic Covered | Key Concepts |
| :--- | :--- | :--- |
| 📄 [requirements.txt](./fastapi_learning/requirements.txt) | Dependencies | FastAPI, Uvicorn, Pydantic, pyjwt, bcrypt, httpx dependencies list |
| 📄 [01_fastapi_basics.py](./fastapi_learning/01_fastapi_basics.py) | Routes & Params | Basic setup, Get/Post routes, Path parameters, Query parameters, Request Body |
| 📄 [02_pydantic_schemas.py](./fastapi_learning/02_pydantic_schemas.py) | Pydantic Validation | Nested Schemas, Field constraints, Custom field validators, JSON parsing |
| 📄 [03_dependency_injection.py](./fastapi_learning/03_dependency_injection.py) | Depends System | Config Dependency, DB connection managers (`yield` pattern), API Key validation |
| 📄 [04_async_endpoints_and_background.py](./fastapi_learning/04_async_endpoints_and_background.py) | Async & Workers | Non-blocking async endpoints vs sync endpoints, `BackgroundTasks` queue trigger |
| 📄 [05_webhooks_and_integrations.py](./fastapi_learning/05_webhooks_and_integrations.py) | Integrations | Incoming Webhook payload handlers, Outgoing async API calls using `httpx.AsyncClient` |
| 📂 [task_manager/](./fastapi_learning/task_manager) | Practical Project | Task Manager API. Includes Mock Database, Pydantic schemas, password hashing, JWT Authentication, CRUD endpoints, and asynchronous background email notification handlers. |

---

## ⚡ How to Run the Code

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Sonff/Learning_automation.git
   cd Learning_automation
   ```

2. **Setup virtual environment (recommended):**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r fastapi_learning/requirements.txt
   ```

4. **Run any module file directly:**
   For example, to run the **Task Manager API Project**:
   ```bash
   # From the project root, run:
   uvicorn fastapi_learning.task_manager.main:app --reload
   ```
   Open `http://127.0.0.1:8000/docs` in your browser to interact with the API Swagger UI.

---

## 🔮 Future Modules (Coming Soon...)
*   `vector_db_rag/` - RAG models using vector stores.
*   `ai_agents_langgraph/` - Autonomous stateful agents.
*   `deployment/` - Docker configurations and cloud CI/CD pipelines.

---

*Made with 💻 by [Sonff](https://github.com/Sonff).*

