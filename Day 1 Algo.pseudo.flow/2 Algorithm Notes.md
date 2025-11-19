# Algorithm
### What is an Algorithm?

An **algorithm** is a step-by-step sequence of instructions to solve a specific problem or perform a task.  
Think of it as a **recipe** – just like making tea or a sandwich!

**Example (everyday life):**
- Recipe for making tea
- Steps to make a sandwich
- Directions to reach school from home

**Key Point:**  
An algorithm is written in **simple human language** (or pseudo-code), **not** in any programming language.

---

### Types of Algorithms

| Type            | Description                                                                 | Example                              |
|-----------------|-----------------------------------------------------------------------------|--------------------------------------|
| **Sequential**     | Instructions are executed one after another in order. No skipping, no repetition. | Recipe for boiling water             |
| **Conditional (Branching)** | Uses decisions (if-else). Some steps may be skipped depending on a condition. | Check if a number is even or odd     |
| **Iterative (Looping)**    | Repeats a block of steps until a condition is met.                          | Summing numbers from 1 to 100        |

**Note:** Most real-world algorithms combine all three types.

---

### Characteristics of a Good Algorithm

A good algorithm must have the following properties:

| # | Characteristic                | Meaning                                                                 |
|---|-------------------------------|-------------------------------------------------------------------------|
| 1 | **Clear and Simple**          | Easy to understand by humans                                            |
| 2 | **Finite Steps**              | Must terminate after a limited number of steps (no infinite loops)      |
| 3 | **Well-Defined Input**        | Clearly specified what input it accepts (can be zero inputs)            |
| 4 | **Well-Defined Output**       | Clearly specified what result it produces                               |
| 5 | **Effective**                 | Each step must be basic enough to be carried out exactly (by human or computer) |
| 6 | **Unambiguous**               | Every step must have only one meaning                                   |

---

### Visual Representation of Algorithm Types

```mermaid
flowchart TD
    A[Sequential Algorithm] --> B[Step 1]
    B --> C[Step 2]
    C --> D[Step 3]
    D --> E[End]

    F[Conditional Algorithm] --> G{Condition?}
    G -- Yes --> H[Do This]
    G -- No --> I[Do That]
    H --> J[End]
    I --> J

    K[Iterative Algorithm] --> L[Initialize]
    L --> M{Condition?}
    M -- Yes --> N[Repeat Steps]
    N --> M
    M -- No --> O[End]