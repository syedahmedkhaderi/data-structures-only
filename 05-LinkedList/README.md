# Linked List Implementations in Python

My first comprehensive learning project demonstrating all types of **linked lists** using Python — featuring various implementations:

- Singly Linked List
- Doubly Linked List
- Circular Linked List (Singly & Doubly)
- Reversal Operation (Singly)
- Dictionary-Based Linked List (non-classic, more intuitive)

## What’s Inside

| Data Structure                | Features                                                    |
|-------------------------------|-------------------------------------------------------------|
| Singly Linked List            | Append, Prepend, Insert, Delete, Reverse, Get, Update       |
| Doubly Linked List            | Bidirectional traversal, Append, Prepend, Insert, Delete, Search, Get, Set |
| Circular Linked List (Singly) | Last node points to head, Append, Prepend, Insert, Remove, Search, Update |
| Circular Doubly Linked List   | Circular with prev/next pointers, Insert, Delete, Traversal (forward/reverse) |
| Dictionary-Based List         | Simplified syntax using dicts and key access                |

## Folder Structure

```
6-LinkedList/
├── 1-Singly LL/
│   └── singly_linked_list.py
├── 2-Doubly LL/
│   └── doubly_linked_list.py
├── 3-Circular LL/
│   ├── circular_linked_list.py
│   └── CircularDoublyLinkedList.py
├── dict_linked_list.py
├── Reverse_SLL.py
└── README.md
```

## Dictionary-Based Linked List

**Location:** `dict_linked_list.py`

A more Pythonic and beginner-friendly variation using dictionaries instead of Node objects.

### Methods Implemented:

- `__init__(value)` - Initialize with a head node
- `append(data)` - Add element to the end
- `prepend(data)` - Add element to the beginning
- `insert(index, value)` - Insert value at specific index
- `delete(index)` - Delete node at given index
- `get_index(index)` - Return the node (dictionary) at given index
- `print_list()` - Return list of all values in order
- `help()` - Display help message with all methods

### Key Features:

- No object-oriented Node class required
- All nodes are simple Python dictionaries
- Easier to debug and visualize for beginners
- Uses dictionary access methods instead of dot notation
- Great for learning linked list concepts without OOP complexity


## Concepts Covered

- **Singly Linked Lists** - Basic linked list with forward-only traversal
- **Doubly Linked Lists** - Bidirectional traversal with prev/next pointers
- **Circular Linked Lists** - Both singly and doubly circular variations
- **Object-Oriented vs Dictionary-Based** - Different implementation approaches
- **Pointer Manipulation** - Understanding and managing node references
- **Reversal Logic** - In-place list reversal algorithms
- **Edge Case Handling** - Empty lists, single nodes, boundary conditions
- **Dynamic Memory Modeling** - Understanding how nodes are scattered in memory


## Requirements

- Python 3.7+
- No external libraries required
- Runs directly on the CLI or any Python interpreter

## License

This project is licensed under the **MIT License** — free to use, modify, and share.

