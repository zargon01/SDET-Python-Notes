## Table of Contents
1. [Variables in Python](#variables-in-python)
   - What is a Variable?
   - Why are Variables used?
   - When are Variables used?
   - Where are Variables used in Python?
   - How are Variables used? (Declaration, Naming Rules, Examples)
2. [Data Types in Python](#data-types-in-python)
   - What is a Data Type?
   - Why are Data Types used?
   - When do we choose specific Data Types?
   - Where are Data Types relevant in Python?
   - How are Data Types used? (Built-in types with examples)
3. [References](#references)

---

## Variables in Python

### What is a Variable?
A **variable** is a named storage location in memory that holds a value or a reference to an object.  
In Python, variables are symbolic names (identifiers) chosen by the programmer that allow referencing stored data throughout the program.

**Key Point**: Unlike languages like C/C++/Java, Python variables do **not** store the value directly — they store **references** to objects. Everything in Python is an object.

### Why are Variables used?
- To store and manipulate data dynamically during program execution.
- To make code readable and maintainable by giving meaningful names to values.
- To allow programs to remember user input, intermediate results, configuration, etc.
- To enable reusability of values without hardcoding them.

### When are Variables used?
Variables are used whenever a program needs to:
- Process changing or unknown values (user input, calculations, API responses)
- Store intermediate or final results
- Create dynamic, interactive, and reusable logic
- Manage state in loops, functions, classes, or throughout the entire program lifecycle

### Where are Variables used in Python?
- In **global scope** (module level)
- In **local scope** (inside functions or classes)
- As **instance variables** (inside objects/classes)
- As **class variables** (shared across instances)
- In comprehensions, generators, lambdas, and closures

Python uses **dynamic typing** — you don’t declare the type beforehand; it is determined at runtime.

### How are Variables used?

#### Naming Rules & Conventions
- Case-sensitive (`age` ≠ `Age`)
- Must start with a letter or underscore `_`
- Can contain letters, digits, and underscores
- Cannot be a Python reserved keyword (`def`, `class`, `for`, etc.)

**Valid names**:
```python
age = 25
_user_name = "Alice"
myVariable = "camelCase"
my_variable = "snake_case"      
MyVariable = "PascalCase"
__private_var = 42              
```

#### Declaration & Assignment
```python
# Simple assignment creates the variable
name = "Alice"          # str
age = 30                # int
height = 5.9            # float
is_student = True       # bool
```

#### Reassignment
```python
age = 30
age = 31                # Now points to a new integer object
age = "thirty-one"      # Can even change type! (dynamic typing)
```

#### Using Variables
```python
full_name = name + " Smith"
next_year_age = age + 1
print(f"{full_name} will be {next_year_age} next year.")
```

#### Multiple Assignment
```python
x, y, z = 1, 2, 3
a = b = c = 0
```

---

## Data Types in Python

### What is a Data Type?
A data type defines the kind of value a variable can hold and what operations are allowed on it.  
Python has built-in data types that classify data items and determine behavior.

### Why are Data Types used?
- To ensure correct operations (e.g., you can’t add a string and a list without conversion)
- Memory efficiency and performance
- Code clarity and self-documentation
- Enable Python’s dynamic but safe type system

### When do we choose specific Data Types?

| Situation                     | Recommended Type |
|------------------------------|------------------|
| Whole numbers               | `int`           |
| Decimal/fractional numbers  | `float`         | 
| Complex mathematical ops    | `complex`       |
| Text data                   | `str`           | 
| Ordered, mutable collection | `list`          |
| Ordered, immutable collection| `tuple`        |
| Unordered unique items      | `set`           | 
| Key-value mappings          | `dict`          |
| Truth values                | `bool`          |

### Where are Data Types relevant in Python?
- During assignment (type is bound to the object, not the variable)
- In function signatures (type hints with `-> int`, `List[str]`, etc.)
- In built-in functions and methods
- When checking with `type()` or `isinstance()`
- When objects are used as dictionary keys (must be hashable → immutable types)

### How are Data Types used?

#### Built-in Data Types Summary & Examples
```python
# 1. Numeric Types
a = 42                  # int
b = 3.14159             # float
c = 2 + 3j              # complex

# 2. Sequence Types
s = "Hello Python"              # str (immutable)
names = ["Alice", "Bob", 42]    # list (mutable, heterogeneous)
coordinates = (10, 20)          # tuple (immutable)

# 3. Mapping Type
person = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL"]
}                               # dict (mutable, ordered since 3.7)

# 4. Set Types
unique = {1, 2, 2, 3, 4}        # set → {1, 2, 3, 4} (unordered, no duplicates)
frozen = frozenset([1, 2, 3])   # frozenset (immutable, hashable)

# 5. Boolean Type
is_active = True                # bool
is_valid = False

# 6. Binary Types (less common)
byte_data = b"hello"            # bytes (immutable)
mutable_bytes = bytearray(b"hi")# bytearray (mutable)
```

#### Checking Types
```python
print(type(age))        # <class 'int'>
print(isinstance(names, list))  # True
print(isinstance(coordinates, tuple))  # True
```

#### Type Conversion (Casting)
```python
str(42)      # → "42"
int("100")   # → 100
float(5)     # → 5.0
list("abc")  # → ['a', 'b', 'c']
set([1,2,2]) # → {1, 2}
```

---

## References

### Variables
- [LearnPython - Variables and Types](https://www.learnpython.org/en/Variables_and_Types)
- [W3Schools - Variables](https://www.w3schools.com/programming/prog_variables.php)
- [Corporate Finance Institute - Python Variables](https://corporatefinanceinstitute.com/resources/data-science/python-variables/)
- r/ProgrammerHumor
- r/Python
- r/learnpython
- r/askprogramming

### Data Types
- [Official Python Docs](https://docs.python.org/3/library/datatypes.html)
- [GeeksforGeeks - Python Data Types](https://www.geeksforgeeks.org/python/python-data-types/)
- [W3Schools - Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
- [DigitalOcean - Python Data Types](https://www.digitalocean.com/community/tutorials/python-data-types)
- [Real Python - Python Data Types](https://realpython.com/python-data-types/)
- r/learnpython
- r/PythonLearning
- r/Python

