# Functions

## What is a Function?
A **function** is a reusable block of code that performs a specific task.  
Instead of writing the same code multiple times, we define it once in a function and call it whenever needed.

### Basic Syntax
```python
def function_name():
    # block of code (indented)
    pass
```

### How to Call a Function
```python
function_name()  # parentheses are mandatory
```

## Why Do We Need Functions?
- **Reusability** – Write once, use multiple times
- **Readability** – Code becomes cleaner and easier to understand
- **Debugging** – Easier to find and fix bugs in smaller chunks
- **Code Organization** – Logical separation of tasks
- **Modularity** – Divide large programs into smaller, manageable pieces
- **Team Collaboration** – Different people can work on different functions

## When Should You Use a Function?
- When a task is repeated multiple times
- When logic is complex or lengthy
- When you want to divide a program into modules
- When you want to reuse code with different inputs
- When testing individual parts of the program

## How to Use Functions?
1. Define the function
2. Call the function (as many times as needed)

## Types of Functions in Python

### 1. No Parameters, No Return Value
Performs an action but doesn't take input or return anything.
```python
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!
```

### 2. With Parameters, No Return Value
Accepts input but doesn't return anything.
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### 3. No Parameters, With Return Value
Doesn't take input but returns a value.
```python
def get_pi():
    return 3.14159

result = get_pi()
print(result)  # 3.14159
```

### 4. With Parameters, With Return Value (Most Common)
Accepts input and returns output.
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

### 5. Function with Default Parameters
Parameters have default values if no argument is passed.
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet()          # Hello, Guest!
```
**Note:** Default parameters must come after non-default ones.

## *args and **kwargs

### *args – Variable Number of Positional Arguments
Allows passing any number of arguments. Inside the function, *args is a tuple.
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))   # 15
print(sum_all(10, 20))          # 30
```

### **kwargs – Variable Number of Keyword Arguments
Allows passing any number of named arguments. Inside the function, **kwargs is a dictionary.
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Delhi")
# Output:
# name: Alice
# age: 25
# city: Delhi
```

### Combining *, **, and normal parameters
```python
def example(a, b, *args, **kwargs):
    print(a, b)
    print(args)    # tuple
    print(kwargs)  # dict

example(1, 2, 3, 4, 5, x=10, y=20)
```
Order must be: normal params → *args → **kwargs

## Pass by Value vs Pass by Reference in Python
Python uses "Pass by Object Reference" (not exactly call-by-value or call-by-reference).

| Object Type | Behavior | Original Object Changes? |
|-------------|----------|---------------------------|
| Immutable (int, float, str, tuple, frozenset) | Behaves like Pass by Value | No |
| Mutable (list, dict, set) | Behaves like Pass by Reference | Yes |

### Example:
```python
# Immutable (int)
def modify(x):
    x = 100

num = 10
modify(num)
print(num)  # 10 (unchanged)

# Mutable (list)
def modify_list(lst):
    lst.append(100)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 100] (changed)
```

## Scope of Variables

### 1. Local Scope
Variable declared inside a function. Only accessible inside that function.
```python
def func():
    x = 10    # local variable
    print(x)

func()  # 10
# print(x)  → NameError
```

### 2. Global Scope
Variable declared outside any function or with the global keyword.
```python
x = 100  # global variable

def func():
    print(x)  # can read global variable

func()  # 100
```

### Modifying Global Variable Inside Function
```python
x = 100

def func():
    global x   # must declare to modify global variable
    x = 200

func()
print(x)  # 200
```

### nonlocal keyword (for nested functions)
Used to modify variables in enclosing (not global) scope.
```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    inner()  # 1
    inner()  # 2
```

## Recursion
When a function calls itself directly or indirectly.

Essential Parts of Recursion:
- **Base Case** – Condition to stop recursion
- **Recursive Case** – Function calls itself with a smaller input

### Example: Factorial
```python
def factorial(n):
    if n == 0 or n == 1:     # Base case
        return 1
    return n * factorial(n-1)  # Recursive case

print(factorial(5))  # 120
```

### Corrected Fibonacci
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 0, 1, 1, 2, 3, 5, 8, 13, ...
print(fibonacci(6))  # 8
```
**Warning:** Recursion has limits (~1000 depth by default in Python). Use loops for very large inputs.

## Summary Table

| Feature | Keyword/Concept | Use Case |
|---------|-----------------|----------|
| Default arguments | def func(x=10) | Optional parameters |
| Variable arguments | *args | Unknown number of positional args |
| Keyword variable args | **kwargs | Unknown number of named args |
| Modify global variable | global x | Change variable outside function |
| Modify enclosing variable | nonlocal x | In nested functions |
| Stop recursion | Base case | Prevent infinite recursion |
