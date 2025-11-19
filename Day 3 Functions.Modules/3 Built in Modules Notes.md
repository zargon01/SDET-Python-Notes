# Built-in Modules

## What are Built-in Modules?
Built-in modules are pre-written Python files provided by Python itself.  
They come with every Python installation — no need to install anything.

**Why use them?**
1. Save development time
2. Highly optimized & fast (written in C)
3. Well-tested and reliable
4. Clean and organized code
5. Standard across all platforms

---

## 1. `os` Module – Interact with the Operating System

Used to perform OS-related tasks like working with files, folders, paths, etc.

### Common Functions
```python
import os

# Get current working directory
print(os.getcwd())                

# Change directory
os.chdir("/path/to/folder")

# Create a folder
os.mkdir("new_folder")            # single folder
os.makedirs("parent/child", exist_ok=True)  # nested folders

# Remove file / folder
os.remove("file.txt")             # delete file
os.rmdir("empty_folder")          # delete empty folder
os.removedirs("parent/child")    # remove nested empty folders

# List contents of directory
print(os.listdir("."))           # current folder

# Check if path exists
print(os.path.exists("file.txt")) # True / False

# Join paths (platform independent)
path = os.path.join("folder", "subfolder", "file.txt")
print(path)                       # Works on Windows & Linux/Mac

# Get file name / directory name
print(os.path.basename("/home/user/file.txt"))  # file.txt
print(os.path.dirname("/home/user/file.txt"))   # /home/user
```

---

## 2. `math` Module – Mathematical Functions & Constants
```python
import math

print(math.pi)            # 3.141592653589793
print(math.e)             # 2.718281828459045

print(math.sqrt(16))      # 4.0
print(math.pow(2, 3))     # 8.0
print(math.factorial(5))  # 120

print(math.sin(math.radians(30)))  # 0.5
print(math.cos(math.pi))           # -1.0

print(math.ceil(4.2))     # 5
print(math.floor(4.8))    # 4
print(math.trunc(4.9))    # 4 (removes decimal)

print(math.gcd(48, 18))   # 6 (Greatest Common Divisor)
print(math.log(100, 10))  # 2.0
```

---

## 3. `json` Module – Work with JSON Data
**JSON = JavaScript Object Notation**  
Lightweight, human-readable format for data exchange.

### Key Methods
```python
import json

# Python dict → JSON string
data = {"name": "Alice", "age": 25, "city": "Delhi"}
json_string = json.dumps(data, indent=2)
print(json_string)

# JSON string → Python dict
json_text = '{"name": "Bob", "age": 30}'
python_dict = json.loads(json_text)
print(python_dict["name"])  # Bob

# Write Python object to JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON file into Python object
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data)
```





---

## 4. NumPy – Numerical Python (Third-Party but Essential)
Fast array processing & mathematical operations.  
**Installation:** `pip install numpy`
```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# Properties
print(arr.size)      # 5
print(arr.shape)     # (5,)
print(arr.dtype)     # int64 or int32

# Special arrays
print(np.zeros((3, 3)))
print(np.ones((2, 4)))
print(np.eye(3))                 # 3x3 identity matrix
print(np.arange(0, 10, 2))       # [0 2 4 6 8]
print(np.linspace(0, 1, 5))      # 5 values from 0 to 1

# Math operations (element-wise)
print(arr + 10)
print(arr * 2)
print(np.sqrt(arr))
```

---

## 5. Pandas – Data Manipulation & Analysis
Built on top of NumPy. Best for working with tabular data.  
**Installation:** `pip install pandas`
```python
import pandas as pd

# Series (1D labeled array)
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)

# DataFrame (2D table)
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}
df = pd.DataFrame(data)
print(df)

# Basic operations
print(df.head(2))          # first 2 rows
print(df.info())           # summary
print(df.describe())       # statistical summary
print(df["Name"])          # select column
print(df.loc[0])           # row by index label
print(df.iloc[1])          # row by position
```

---

## Quick Reference Table
| Module    | Purpose                | Key Functions/Classes                     | Install?       |
|-----------|------------------------|-------------------------------------------|---------------|
| os        | OS interaction         | mkdir, remove, path.join, getcwd         | Built-in      |
| math      | Math constants & funcs | pi, sqrt, sin, ceil, gcd                 | Built-in      |
| json      | JSON ↔ Python          | dumps, loads, dump, load                 | Built-in      |
| numpy     | Fast arrays & math     | array, zeros, linspace, sqrt             | pip install   |
| pandas    | Data analysis (tables) | DataFrame, Series, read_csv              | pip install   |

---

