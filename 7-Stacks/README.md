# Stack Implementations in Python

A focused collection of **stack data structures** implemented in Python — showcasing multiple approaches to building and working with LIFO collections for different learning goals.

- Array-Based Stack (dynamic list wrapper)
- Linked List Stack (pointer-based nodes)
- MultiStack (three logical stacks in one array)

## What’s Inside

| Data Structure            | Features                                                                 |
|---------------------------|--------------------------------------------------------------------------|
| Array-Based Stack         | Push, Pop, Peek, Is Empty, Print, Clear, Size, String representation      |
| Linked List Stack         | Node-based Push/Pop, Peek, Is Empty, Traversal, Clear, Size tracking      |
| MultiStack (Three-in-One) | Fixed-size partitioned array, Push/Pop/Peek per stack, Bounds checking   |

## Folder Structure

```
7-Stacks/
├── MultiStack.py
├── stacks_Array_implementation.py
└── stacks_LL_implementation.py
```

## MultiStack Highlight
Implements three independent stacks inside a single array by dividing storage into equal segments. Each stack maintains its own size counter and index calculations to support `Push`, `Pop`, `Peek`, `IsEmpty`, and `IsFull` operations while sharing memory efficiently.

## Concepts:
- **LIFO Fundamentals** – Understanding the core behavior of stack operations
- **Dynamic Array Stacks** – Leveraging Python lists for stack behavior
- **Linked List Backing** – Managing stack nodes with explicit pointers
- **Memory Partitioning** – Hosting multiple stacks within one contiguous array
- **Error Handling** – Guarding against overflow and underflow conditions

## Requirements
- Python 3.7+
- No external libraries required
- Runs directly on the CLI or any Python interpreter

## 📝 License
This project is licensed under the **MIT License** — free to use, modify, and share.