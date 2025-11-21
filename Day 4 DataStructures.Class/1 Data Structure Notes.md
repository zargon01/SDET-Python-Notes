# Data Structures
Python provides 4 primary built-in data structures to store and organize data efficiently:

| Data Structure | Ordered | Mutable | Duplicates Allowed | Indexing | Use Case |
|----------------|--------|--------|--------------------|----------|---------|
| **List**       | Yes    | Yes    | Yes                | Yes      | Dynamic, changeable collections |
| **Tuple**      | Yes    | No     | Yes                | Yes      | Fixed, immutable collections |
| **Set**        | No     | Yes    | No                 | No       | Unique elements, mathematical ops |
| **Dictionary** | Yes*   | Yes    | No (keys)          | By key   | Key-value mappings (fast lookup) |

> *Dictionary maintains insertion order since Python 3.7+

---

## 1. List `[ ]` - Ordered, Mutable, Allows Duplicates

```python
my_list = [10, 20, 30, "hello", 10]
```

### Features
- Maintains insertion order
- Indexed (0-based)
- Allows duplicate elements
- Dynamic size

**When to use?**
- Need ordered collection
- Frequent insertion/deletion/updation
- Need indexing/slicing

### Common Methods
| Method | Description | Example |
|--------|-------------|---------|
| append(x) | Add item at the end | list.append(50) |
| extend(iterable) | Add multiple items from another iterable | list.extend([6,7,8]) |
| insert(i, x) | Insert item at specific index | list.insert(0, 100) |
| remove(x) | Remove first occurrence of x | list.remove(10) |
| pop([i]) | Remove and return item at index (default last) | list.pop() or list.pop(2) |
| clear() | Remove all items | list.clear() |
| index(x) | Return first index of x | list.index(30) |
| count(x) | Count occurrences of x | list.count(10) |
| sort() | Sort list in-place (ascending) | list.sort() |
| sort(reverse=True) | Sort descending | list.sort(reverse=True) |
| reverse() | Reverse the list | list.reverse() |
| copy() | Return shallow copy | new = list.copy() |
| len(list) | Get number of elements | len(my_list) |

### Updating a value
```python
index = my_list.index("hello")
my_list[index] = "hi"
# OR directly
my_list[2] = "new value"
```

### Looping
```python
for item in my_list:
    print(item)

# With index
for i, item in enumerate(my_list):
    print(i, item)
```

---

## 2. Tuple `( )` - Ordered, Immutable, Allows Duplicates
```python
my_tuple = (10, 20, "apple", 10)
single = (5,)   # Note the comma! Otherwise it's just an int
```

**Important**
- (5) → integer
- (5,) → tuple with one element

### Features
- Ordered & Indexed
- Immutable (cannot modify after creation)
- Faster than lists
- Uses less memory
- Can be used as dictionary keys

**When to use?**
- Data should not change (e.g., coordinates, RGB colors, days of week)
- Need hashable type (for dict keys or sets)

### Methods
| Method | Description | Example |
|--------|-------------|---------|
| count(x) | Count occurrences | t.count(10) |
| index(x) | First index of x | t.index("apple") |

### Operations Allowed
```python
# Slicing
print(my_tuple[1:4])

# Concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2  # (1,2,3,4)

# Repetition
t4 = t1 * 3   # (1,2,1,2,1,2)

# Membership
print(20 in my_tuple)

# Length
len(my_tuple)
```

---

## 3. Set `{ }` - Unordered, Mutable, Unique Elements Only
```python
my_set = {10, 20, 30, 10}   # → {10, 20, 30}
empty_set = set()           # Correct way to create empty set
# {} creates empty dict, not set!
```

### Features
- No duplicates
- Unordered (no indexing)
- Very fast membership testing (in operator)
- Supports mathematical set operations

**When to use?**
- Remove duplicates from a list → set(list)
- Fast lookup: if x in my_set:
- Union, intersection, difference operations

### Methods
| Method | Description |
|--------|-------------|
| add(x) | Add element |
| remove(x) | Remove x (raises KeyError if not found) |
| discard(x) | Remove x (no error if not found) |
| pop() | Remove and return arbitrary element |
| clear() | Remove all elements |
| update(iterable) | Add multiple elements |

### Set Operations
| Operation | Code | Meaning |
|-----------|------|---------|
| Union | `set1 | set2` or `set1.union(set2)` | All elements |
| Intersection | `set1 & set2` or `set1.intersection(set2)` | Common elements |
| Difference | `set1 - set2` or `set1.difference(set2)` | In set1 but not in set2 |
| Symmetric Difference | `set1 ^ set2` or `set1.symmetric_difference(set2)` | In either but not both |
| Subset | `set1 <= set2` | All elements of set1 in set2 |
| Superset | `set1 >= set2` | set1 contains set2 |


---

## 4. Dictionary `{key: value}` - Ordered (since 3.7), Mutable, Key-Value Pairs
```python
my_dict = {"name": "Alice", "age": 25, 1: "one"}
empty_dict = {}
```

### Rules for Keys
- Must be immutable and unique
- Allowed: strings, numbers, tuples (containing immutables)
- Not allowed: lists, sets, dicts

### Features
- Fast lookup by key O(1)
- Insertion order preserved (Python 3.7+)
- Keys are unique → duplicate key overwrites previous value

### Common Methods
| Method | Description | Example |
|--------|-------------|---------|
| get(key, default) | Safe access (returns default if key missing) | dict.get("age", 0) |
| keys() | Returns view of all keys | dict.keys() |
| values() | Returns view of all values | dict.values() |
| items() | Returns view of (key, value) tuples | dict.items() |
| update(other) | Merge another dict (overwrites existing keys) | dict.update({"age": 30}) |
| pop(key) | Remove and return value for key | dict.pop("name") |
| popitem() | Remove and return last inserted item (LIFO) | dict.popitem() |
| clear() | Remove all items | dict.clear() |
| copy() | Shallow copy | new = dict.copy() |

### Accessing & Updating
```python
# Access
print(my_dict["name"])
print(my_dict.get("city", "Not found"))  # safer

# Update / Add
my_dict["age"] = 26
my_dict["city"] = "Delhi"

# Delete
del my_dict["age"]
```

### Looping Techniques
```python
# Keys
for key in my_dict:
    print(key)

# Key-Value pairs (recommended)
for key, value in my_dict.items():
    print(key, "→", value)

# Unpacking
for k, v in my_dict.items():
    print(f"{k}: {v}")
```

### Dictionary Comprehension
```python
squares = {x: x*x for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Quick Comparison Summary
| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| Syntax | [ ] | ( ) | { } or set() | {k:v} |
| Ordered | Yes | Yes | No | Yes (3.7+) |
| Mutable | Yes | No | Yes | Yes |
| Allows Duplicates | Yes | Yes | No | No (keys) |
| Indexing | Yes | Yes | No | By key |
| Fast Lookup | O(n) | O(n) | O(1) | O(1) |
| Best For | Sequences | Fixed data | Unique items | Key-value maps |
