### **Lab: Understanding and Using Python Modules**

#### **Objective**
This lab will help you understand how to:
1. **Create and import your own modules**
2. **Use different import techniques (`import`, `from ... import`, aliases)**
3. **Explore module properties (`__name__`, `__file__`, `dir()`)**
4. **Use the `if __name__ == "__main__"` construct**
5. **Import and use built-in modules**

---

### **🔬 Task 1: Creating and Importing Your Own Module**
#### **Starter Code (Faulty & Incomplete)**
1. Create a Python file named `mymodule.py` with the following code:
```python
"""This is a sample module for the lab."""

print("Hello! I am the mymodule module.")

def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

class Scientist:
    """A simple class representing a scientist."""
    
    def __init__(self, name, field):
        self.name = name
        self.field = field

    def __str__(self):
        return f"{self.name} is a scientist in the field of {self.field}."
```

---

#### **Your Task: Import and Use the Module**
Now, in a separate script (`main.py`), do the following:
1. **Import `mymodule`** and call `greet("Alice")`.
2. **Create an instance** of `Scientist` and print it.
3. **Use `dir(mymodule)`** to list module attributes.
4. **Print the module’s `__name__` and `__doc__`.**
5. **Modify `mymodule.py`** so it prints `"This should only run when executed directly"` **only** when executed as `__main__`.

---

### **🔬 Task 2: Experiment with Importing Techniques**
Modify `main.py` to:
1. Use `from mymodule import greet` and call `greet("Bob")` without `mymodule.`.
2. Import `Scientist` as `Sci` and create a scientist object using `Sci("Dr. Eve", "Physics")`.
3. Use `import mymodule as mod` and call `mod.greet("Charlie")`.

---

### **🔬 Task 3: Importing Built-in Modules**
Modify `main.py` to:
1. Import `sys` and print `sys.version`.
2. Import `math` and print the square root of 25.
3. Import `random` and generate a random integer between 1 and 100.

---

### **🔬 Task 4: Using the `__main__` Construct**
Modify `mymodule.py`:
1. Move the greeting message inside a `main()` function.
2. Use:
```python
if __name__ == "__main__":
    main()
```
3. Run both:
   - `python mymodule.py` → should print the greeting.
   - `python main.py` → should **not** print the greeting from `mymodule`.

---

### **✅ Expected Output (After Completing the Lab)**
```text
Hello! I am the mymodule module.  # This appears when first imported

Hello, Alice!
Alice is a scientist in the field of Biology.
['Scientist', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'greet']
Module Name: mymodule
Module Doc: This is a sample module for the lab.

Hello, Bob!
Dr. Eve is a scientist in the field of Physics.
Hello, Charlie!

Python Version: 3.11.2
Square root of 25: 5.0
Random number: 73
```

---

### **Final Deliverables**
✅ `mymodule.py` (modified with `__main__`)  
✅ `main.py` (importing and using `mymodule`, built-in modules, and different import techniques)  

---

