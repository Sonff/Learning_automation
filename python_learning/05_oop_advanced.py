# =====================================================================
# TOPIC 5: ADVANCED OBJECT-ORIENTED PROGRAMMING (OOP)
# =====================================================================
# LangChain base models ko extend karne, Pydantic templates custom 
# class validation, and standard enterprise structures design karne ke 
# liye advanced OOP concepts standard hain.

# ---------------------------------------------------------------------
# 1. Inheritance (Inherit parent properties and behaviors)
# ---------------------------------------------------------------------
# Parent Class (Base Class)
class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        
    def execute(self) -> str:
        raise NotImplementedError("Subclasses must implement the execute method!")

# Child Class (Derived Class)
class SearchAgent(BaseAgent):
    def __init__(self, name: str, search_engine: str):
        # super() parent class ke constructor ya methods call karne ke liye use hota hai.
        super().__init__(name)
        self.search_engine = search_engine
        
    # Overriding the parent's method (Polymorphism)
    def execute(self) -> str:
        return f"Agent {self.name} is searching on {self.search_engine}..."

print("--- 1. Inheritance & Method Overriding ---")
agent = SearchAgent(name="GoogleSearchBot", search_engine="Google Search API")
print(agent.execute())
print()


# ---------------------------------------------------------------------
# 2. Encapsulation & Private Attributes
# ---------------------------------------------------------------------
# Python me strict private keywords nahi hote, but:
# Single underscore `_` variables standard warning hain: "Internal use only".
# Double underscore `__` variables name-mangling start karte hain to avoid access.

class Vault:
    def __init__(self, key: str):
        self.__secret_key = key # Private Attribute
        
    # Getter method to safely read private attribute
    def get_key(self) -> str:
        return f"Masked-Key: {self.__secret_key[:3]}..."

print("--- 2. Encapsulation ---")
my_vault = Vault("my_super_secure_key_123")
# print(my_vault.__secret_key) # Ye ERROR dega (AttributeError)
print(my_vault.get_key()) # Safe way
# Direct bypass name mangling (avoid doing this):
print(f"Bypassed Access: {my_vault._Vault__secret_key}\n")


# ---------------------------------------------------------------------
# 3. Property Decorators (@property, @attribute.setter)
# ---------------------------------------------------------------------
# Methods ko attribute ki tarah calls karne ka tarika aur validations integrate karna.

class TemperatureController:
    def __init__(self, temp: float):
        self._temp = temp
        
    @property
    def temperature(self):
        return self._temp
        
    @temperature.setter
    def temperature(self, value: float):
        if value < 0.0 or value > 2.0:
            raise ValueError("LLM Temperature must be between 0.0 and 2.0!")
        self._temp = value

print("--- 3. Property Decorators ---")
ctrl = TemperatureController(0.7)
print(f"Current Temp: {ctrl.temperature}") # Read property like attribute (no parentheses)
ctrl.temperature = 1.2 # Set value like normal variable
print(f"New Temp: {ctrl.temperature}")
# ctrl.temperature = 2.5 # Yeh ValueError return karega.
print()


# ---------------------------------------------------------------------
# 4. Dunder (Double Underscore) Methods / Magic Methods
# ---------------------------------------------------------------------
# Built-in operations like printing, comparisons, and calling objects 
# like functions customize karne ke liye magic methods use hote hain.

class VectorDoc:
    def __init__(self, text: str, vector_id: int):
        self.text = text
        self.vector_id = vector_id
        
    # Object user-friendly print (string representation) ke liye:
    def __str__(self):
        return f"Doc(ID={self.vector_id}): '{self.text[:20]}...'"
        
    # Developer debugging details ke liye:
    def __repr__(self):
        return f"VectorDoc(text='{self.text}', vector_id={self.vector_id})"
        
    # Class object ko callable function banane ke liye `__call__`:
    def __call__(self, suffix: str):
        return self.text + " " + suffix

print("--- 4. Dunder (Magic) Methods ---")
doc = VectorDoc("Deep learning models require structured prompt design", 101)
print(str(doc))  # __str__ calls
print(repr(doc)) # __repr__ calls
print(doc("highly automated!")) # __call__ checks (Invoking instance as function)
print()
