# =====================================================================
# TOPIC 4: OBJECT-ORIENTED PROGRAMMING (OOP) FUNDAMENTALS
# =====================================================================
# Python me lagbhag sab kuch object hai. AI Agents, LLM models, aur
# APIs customize karne ke liye Classes design karna seekhna bohot zaroori hai.

# ---------------------------------------------------------------------
# 1. Defining a Class and Constructor (__init__)
# ---------------------------------------------------------------------
class LLMModel:
    """
    LLM Model ki template class jo details store aur print karegi.
    """
    # Constructor: Jab object create hota hai, tab yeh method automatic call hota hai.
    def __init__(self, model_name: str, api_key: str, temperature: float = 0.7):
        self.model_name = model_name  # Instance Attribute
        self.api_key = api_key        # Instance Attribute
        self.temperature = temperature # Instance Attribute
        
    # Instance Method: Jo attributes ko manipulate ya show kare.
    def get_details(self) -> str:
        # Security reason se full api key leak nahi karenge:
        masked_key = self.api_key[:4] + "*" * (len(self.api_key) - 4)
        return f"Model: {self.model_name} | Temp: {self.temperature} | Key: {masked_key}"

print("--- 1. Creating Objects & Accessing Methods ---")
# Instantiating (creating) objects:
gpt_model = LLMModel(model_name="gpt-4o", api_key="sk-proj123456789", temperature=0.2)
claude_model = LLMModel(model_name="claude-3-5-sonnet", api_key="sk-ant987654321")

# Accessing methods:
print(gpt_model.get_details())
print(claude_model.get_details())
print()


# ---------------------------------------------------------------------
# 2. Instance Attributes vs Class Attributes
# ---------------------------------------------------------------------
# Class Attributes: Saare instances (objects) ke liye common hote hain.
# Instance Attributes: Har object ke unique hote hain.

class Agent:
    # Class Attribute (Shared among all agents)
    platform = "OpenAI Swarm Ecosystem"
    
    def __init__(self, agent_name: str, role: str):
        # Instance Attributes (Unique to each agent)
        self.agent_name = agent_name
        self.role = role

print("--- 2. Class vs Instance Attributes ---")
agent1 = Agent("Alice", "Researcher")
agent2 = Agent("Bob", "Writer")

print(f"{agent1.agent_name} is a {agent1.role} on platform: {agent1.platform}")
print(f"{agent2.agent_name} is a {agent2.role} on platform: {agent2.platform}")

# Class attribute change karne se sabhi objects me change reflect hoga if accessed:
Agent.platform = "Custom Agentic Hub"
print(f"Updated platform (Agent 1): {agent1.platform}")
print(f"Updated platform (Agent 2): {agent2.platform}")
print()


# ---------------------------------------------------------------------
# 3. Dynamic Attribute Modification & Adding Custom attributes
# ---------------------------------------------------------------------
print("--- 3. Dynamic Modification ---")
# Aap dynamically attributes change kar sakte hain:
agent1.role = "Lead Researcher"
print(f"Agent 1 new role: {agent1.role}")

# Checking if object has an attribute safely:
if hasattr(agent1, 'role'):
    print(f"Agent has role: {getattr(agent1, 'role')}")
print()
