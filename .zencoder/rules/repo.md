---
description: Repository Information Overview
alwaysApply: true
---

# Data Structures Implementation in Python

## Summary
This repository contains comprehensive Python implementations of various data structures for educational purposes. It includes arrays, lists, hash tables, tuples, linked lists, stacks, queues, trees, and graphs, each with detailed implementations and examples.

## Structure
The repository is organized by data structure type, with each directory containing implementations and examples:
- **2-Arrays**: Array implementations and practice problems
- **3-Lists**: List operations and examples
- **4-HashTable**: Hash table and dictionary implementations
- **5-Tuples**: Tuple operations
- **6-LinkedList**: Various linked list implementations
- **Stacks & Queues**: Stack and queue implementations
- **Trees**: BST, Heap, and Trie implementations
- **Graphs**: Graph data structure implementations
- **timeComplexities.py**: Examples of different time complexities

## Language & Runtime
**Language**: Python
**Version**: Python 3.7+
**Build System**: None (standalone Python scripts)
**Package Manager**: None (no external dependencies)

## Dependencies
**Main Dependencies**:
- No external libraries required
- Standard Python library only

## Main Components

### Linked Lists
**Main Files**: 
- `6-LinkedList/1-Singly LL/singly_linked_list.py`
- `6-LinkedList/2-Doubly LL/doubly_linked_list.py`
- `6-LinkedList/3-Circular LL/circular_linked_list.py`
- `6-LinkedList/dict_linked_list.py`

**Features**:
- Singly, doubly, and circular linked list implementations
- Dictionary-based linked list implementation
- Reversal operations

### Trees
**Main Files**:
- `Trees/BST.py`: Binary Search Tree implementation
- `Trees/Heap/Heap.py`: Heap data structure
- `Trees/Trie.py`: Trie (prefix tree) implementation
- `Trees/priority_queue.py`: Priority queue implementation

**Features**:
- BST operations (insertion, deletion, traversal)
- Min/max heap operations
- Trie for efficient prefix-based retrieval

### Graphs
**Main Files**:
- `Graphs/graphs.py`: Main graph implementation
- `Graphs/minimalist_graphs.py`: Simplified graph implementation

**Features**:
- Undirected graph implementation using adjacency lists
- Methods for node/edge insertion and visualization

### Stacks & Queues
**Main Files**:
- `Stacks & Queues/stacks_Array_implementation.py`
- `Stacks & Queues/stacks_LL_implementation.py`
- `Stacks & Queues/Queue_using_Array.py`
- `Stacks & Queues/Queue_LL_implementation.py`

**Features**:
- Array-based and linked list-based implementations
- Basic operations (push, pop, enqueue, dequeue)

### Hash Tables
**Main Files**:
- `4-HashTable/Hashtable.py`
- `4-HashTable/Dictionary/dictionary1.py`

**Features**:
- Custom hash table implementation
- Dictionary usage examples

## Usage
Each Python file can be run independently:

```bash
python3 <filename>.py
```

For example:
```bash
python3 6-LinkedList/1-Singly\ LL/singly_linked_list.py
python3 Trees/BST.py
python3 Graphs/graphs.py
```

## Educational Content
The repository includes educational materials:
- Time complexity examples in `timeComplexities.py`
- PDF document on Big O notation
- Text files with explanations for complex data structures