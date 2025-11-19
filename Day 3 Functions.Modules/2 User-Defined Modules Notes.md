# User-Defined Modules

## What is a Module?
A **module** is a single Python file (`.py`) that contains:
- Functions
- Variables
- Classes
- Executable code

A **user-defined module** is a module created by you (the programmer), not part of Python’s standard library.

### Built-in Modules vs User-Defined Modules
| Type              | Example                  | Created By          |
|-------------------|--------------------------|---------------------|
| Built-in          | `math`, `os`, `random`   | Python itself       |
| User-Defined      | `my_tools.py`, `utils.py`| You (the programmer)|

---

## Why Do We Need User-Defined Modules?

1. **Code Reusability** – Use the same code in multiple projects
2. **Maintainability** – Fix or improve code in one place
3. **Better Organization** – Separate logic into logical files
4. **Readability** – Cleaner and more understandable project structure
5. **Team Collaboration** – Different team members can work on different modules
6. **Avoid Name Conflicts** – Keep variables/functions isolated

---

## How to Create a User-Defined Module?

**Step 1:** Create a new Python file  
Example: `math_utils.py`

```python
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

company_name = "MyCompany"
```

**Step 2:** Save it in the same folder as your main script  
(or in a folder that Python can find – more on this later)

## How to Use (Import) a Module?

### 1. Basic Import
```python
import math_utils

print(math_utils.add(10, 5))        # 15
print(math_utils.PI)                # 3.14159
```

### 2. Import with Alias (for long names)
```python
import math_utils as mu

print(mu.subtract(10, 5))           # 5
```

### 3. Import Specific Items (Recommended)
```python
from math_utils import add, subtract, PI

print(add(20, 30))                  # 50
print(subtract(100, 40))            # 60
print(PI)                           # 3.14159
```

### 4. Import Everything (Not Recommended in large projects)
```python
from math_utils import *

print(add(5, 5))                    # 10
print(company_name)                 # MyCompany
```
**Warning:** Avoid `from module import *` → can cause name conflicts and make code harder to debug.

---

## Important: __name__ and __main__
When you run a Python file directly, Python sets a special variable `__name__` to `"__main__"`.  
When the file is imported as a module, `__name__` becomes the module name.

### Best Practice: Protect code that should run only when file is executed directly
```python
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# This block runs only when you run the file directly
if __name__ == "__main__":
    print("Testing module directly...")
    print(add(10, 20))
    print("Module is working!")
else:
    print("Module is imported!")
```

**Output when imported:**
```
Module is imported!
```

**Output when run directly (`python math_utils.py`):**
```
Testing module directly...
30
Module is working!
```
This is the standard way to write reusable modules with test code.

---

## Module Search Path
Python looks for modules in these places (in order):

1. Current directory
2. Built-in modules
3. Paths listed in `sys.path`

You can check where Python looks:
```python
import sys
print(sys.path)
```

---

## How to Import from Subfolders?
Create a folder structure:
```
my_project/
├── main.py
└── tools/
    ├── __init__.py      ← Important! Makes it a package
    └── calculator.py
```
Then import like this:
```python
from tools.calculator import add
# or
import tools.calculator as calc
```
`__init__.py` can be empty – it just tells Python "this folder is a package".

---

## Reloading a Module (During Development)
If you modify a module and want to reload it without restarting Python:
```python
import importlib
import math_utils

importlib.reload(math_utils)
```
Useful in Jupyter Notebook or interactive sessions.

---

## Common Module Naming Conventions

- Use lowercase only
- Use underscores (snake_case)
- Avoid using built-in names

**Good names:**
```
data_processor.py, string_utils.py, file_handler.py
```
**Bad names:**
```
MyModule.py (uppercase), import.py (conflicts with keyword)
```

---

## Summary Table

| Import Style      | Syntax Example                              | Best For            | Risk of Conflict |
|-------------------|--------------------------------------------|----------------------|------------------|
| Full module       | `import math_utils`                       | Large modules        | Low              |
| With alias        | `import math_utils as mu`                 | Long names           | Low              |
| Specific items    | `from math_utils import add, PI`          | Clean namespace      | Medium           |
| Everything        | `from math_utils import *`                | Quick testing        | High             |
| From package      | `from tools.calculator import multiply`   | Organized projects   | Low              |

---

