# Flowchart

A **flowchart** is a diagrammatic (graphical) representation of a process, workflow, system, or algorithm. It uses standardized symbols connected by arrows to show the sequence of steps and decision points clearly.

---

### Why Use a Flowchart?

1. **Simplifies complex problems** – Breaks down processes into simple, manageable steps.
2. **Improves communication** – Easy to understand even for non-technical people.
3. **Provides visual thinking aid** – Helps in planning, analyzing, and debugging logic.
4. **Documentation & Training** – Serves as clear documentation for processes and programs.
5. **Identifies bottlenecks & inefficiencies** – Makes it easy to spot redundant or problematic steps.

---

### Types of Flowcharts

| Type                | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| **System Flowchart**     | Shows the flow of data and processes in an entire system (hardware + software). Often used in system analysis. |
| **Program Flowchart**    | Represents the logical flow and sequence of operations in a computer program or algorithm. |
| **Process Flowchart**    | Depicts steps in a business process or workflow (e.g., order processing, manufacturing). Also called **Process Map**. |
| **Document Flowchart**   | Tracks the movement of documents/forms through an organization.         |
| **Data Flow Diagram (DFD)** | Focuses only on data movement (not control flow). Sometimes considered a variant. |

---

### Standard Flowchart Symbols (with Images)

| Symbol              | Name               | Meaning                                                      | Image |
|---------------------|--------------------|--------------------------------------------------------------|-------|
| ![Terminal](https://upload.wikimedia.org/wikipedia/commons/0/0d/Flowchart_Terminal.svg) | **Oval / Terminator** | Start or End of the flowchart                                | ![](https://upload.wikimedia.org/wikipedia/commons/0/0d/Flowchart_Terminal.svg) |
| ![Process](https://upload.wikimedia.org/wikipedia/commons/2/2f/Flowchart_Process.svg) | **Rectangle**         | Process, action, or operation (e.g., calculations, assign value) | ![](https://upload.wikimedia.org/wikipedia/commons/2/2f/Flowchart_Process.svg) |
| ![Input/Output](https://upload.wikimedia.org/wikipedia/commons/9/97/Flowchart_InputOutput.svg) | **Parallelogram**     | Input or Output (e.g., read data, display result)            | ![](https://upload.wikimedia.org/wikipedia/commons/9/97/Flowchart_InputOutput.svg) |
| ![Decision](https://upload.wikimedia.org/wikipedia/commons/2/29/Flowchart_Decision.svg) | **Diamond**           | Decision or branching point (Yes/No or condition check)      | ![](https://upload.wikimedia.org/wikipedia/commons/2/29/Flowchart_Decision.svg) |
| ![Arrow](https://upload.wikimedia.org/wikipedia/commons/c/c3/Flowchart_Arrow.svg) | **Arrow**             | Direction of flow (should not cross or overlap)              | ![](https://upload.wikimedia.org/wikipedia/commons/c/c3/Flowchart_Arrow.svg) |
| ![Connector](https://upload.wikimedia.org/wikipedia/commons/6/6d/Flowchart_Connector.svg) | **Circle (On-page Connector)** | Connects parts of flowchart on the same page                | ![](https://upload.wikimedia.org/wikipedia/commons/6/6d/Flowchart_Connector.svg) |
| ![Off-page Connector](https://upload.wikimedia.org/wikipedia/commons/3/3f/Flowchart_OffPageConnector.svg) | **Pentagon / Off-page Connector** | Links to another page                                       | ![](https://upload.wikimedia.org/wikipedia/commons/3/3f/Flowchart_OffPageConnector.svg) |
| ![Document](https://upload.wikimedia.org/wikipedia/commons/8/87/Flowchart_Document.svg) | **Document**          | Represents a document or report                              | ![](https://upload.wikimedia.org/wikipedia/commons/8/87/Flowchart_Document.svg) |
| ![Database](https://upload.wikimedia.org/wikipedia/commons/5/59/Flowchart_Database.svg) | **Cylinder**          | Represents a database or data storage                        | ![](https://upload.wikimedia.org/wikipedia/commons/5/59/Flowchart_Database.svg) |

---

### Rules for Good Flowcharts

1. Use **only standard symbols**.
2. Flow should generally go **top-to-bottom** and **left-to-right**.
3. Arrows should **never cross** (use connectors if needed).
4. Every path must have a **clear start and end**.
5. Decision diamonds must have **exactly two outgoing paths** (Yes/No).
6. Keep it **simple and readable** – avoid clutter.

---

### Steps to Create a Good Flowchart

1. **Understand the problem statement** completely.
2. Identify **inputs**, **processes**, and **outputs**.
3. Choose the appropriate **type of flowchart**.
4. Break the process into **logical steps**.
5. Select the **correct symbol** for each step.
6. Arrange symbols in a **logical sequence**.
7. Connect symbols with **arrows** showing the flow.
8. Label each symbol clearly.
9. **Dry-run/test** the flowchart with sample data to check correctness.
10. Review and refine for clarity.

---

### Example: Simple Flowchart – Check if a Number is Positive, Negative, or Zero

```mermaid
flowchart TD
    A[Start] --> B[Input Number]
    B --> C{Is Number > 0?}
    C -- Yes --> D[Print "Positive"]
    C -- No --> E{Is Number < 0?}
    E -- Yes --> F[Print "Negative"]
    E -- No --> G[Print "Zero"]
    D --> H[End]
    F --> H
    G --> H