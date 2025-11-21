# Classes & Objects

## What is a Class?
A **class** is a **blueprint** or **template** for creating objects.  
It defines:
- **Attributes** (data/variables)
- **Methods** (functions/behaviors)

```python
class Car:
    pass  # empty class
```

### Naming Convention
Class names should follow PascalCase:
```python
class StudentInfo:
class BankAccount:
class ElectricCar:
```

---

## What is an Object?
An object is an instance of a class.
```python
# Creating objects (instances)
car1 = Car()
car2 = Car()
```
Each object has its own copy of attributes and can call methods.

### Why Do We Need Classes?
- To group related data and functions together
- To create multiple objects with the same structure
- To achieve code reusability and organization
- Foundation of OOP (Object-Oriented Programming)

---

## Constructor in Python: `__init__()`
A special method that runs automatically when an object is created.
```python
class Car:
    def __init__(self):
        print("Object created! Constructor called automatically.")

# Creating object → __init__ runs automatically
c = Car()
# Output: Object created! Constructor called automatically.
```

### Important Rules
- Only one `__init__` method per class
- If you define multiple `__init__`, the last one overwrites previous ones
- Python does not support constructor overloading like Java/C++

### Types of Constructors
1. **Default Constructor (No parameters)**
```python
def __init__(self):
    print("Default constructor")
```

2. **Parameterized Constructor**
Used to initialize instance variables at object creation time.
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand    # instance variable
        self.model = model
        self.year = year

    def display(self):
        print(f"{self.year} {self.brand} {self.model}")

# Creating object with values
my_car = Car("Toyota", "Camry", 2023)
my_car.display()  # 2023 Toyota Camry
```

---

## The `self` Parameter
- `self` represents the current object/instance
- It must be the first parameter in every instance method
- Python automatically passes the object as `self` when method is called

```python
class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print(self.x + self.y)

    def multiply(self):
        return self.x * self.y

m = Math(10, 20)
m.add()        # → 30     (Python does: Math.add(m))
print(m.multiply())  # → 200
```
You can name it anything (not recommended), but `self` is convention:
```python
def __init__(abc, name):
    abc.name = name
```

---

## Types of Variables in a Class
| Type | Defined In | Scope | Example |
|------|-----------|-------|---------|
| Instance Variables | `__init__` or methods | Unique per object | `self.name = "John"` |
| Class Variables | Directly in class | Shared by all objects | `wheels = 4` |

```python
class Car:
    wheels = 4                    # Class variable (shared)

    def __init__(self, brand):
        self.brand = brand        # Instance variable (unique)

c1 = Car("Honda")
c2 = Car("Ford")

print(c1.brand)      # Honda
print(c2.wheels)     # 4
print(Car.wheels)    # 4 (accessed via class)
```

---

## Types of Methods in Python
| Type | First Parameter | Called On | Purpose |
|------|-----------------|-----------|---------|
| Instance Method | `self` | Object | Work with instance data |
| Class Method | `cls` | Class | Work with class data |
| Static Method | None | Class or Object | Utility function (no access to class/object) |

### 1. Instance Method (Most Common)
```python
def show(self):
    print(self.name)
```

### 2. Class Method
Uses `@classmethod` decorator:
```python
class Student:
    college = "ABC University"

    @classmethod
    def get_college(cls):
        return cls.college

print(Student.get_college())
```

### 3. Static Method
Uses `@staticmethod` — doesn't need `self` or `cls`:
```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 7))  # 12
```

---

## Creating Multiple Objects
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and {self.age} years old.")

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.introduce()   # Hi, I'm Alice and 25 years old.
p2.introduce()   # Hi, I'm Bob and 30 years old.
```

---

## Summary Table
| Concept | Syntax / Keyword | Description |
|---------|-------------------|-------------|
| Class | `class Name:` | Blueprint for objects |
| Object | `obj = ClassName()` | Instance of class |
| Constructor | `def __init__(self, ...)` | Called automatically on object creation |
| self | First param in methods | Refers to current object |
| Instance Variable | `self.var` | Unique to each object |
| Class Variable | Defined outside methods | Shared across all objects |
| Instance Method | Uses `self` | Operates on object data |
| Class Method | `@classmethod` + `cls` | Operates on class itself |
| Static Method | `@staticmethod` | Utility function, no access to class/object |
