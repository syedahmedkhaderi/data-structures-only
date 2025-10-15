## Table of Contents

- [Queue](#queue)
  - [Queue (No Size Limit)](#queue-no-size-limit)
  - [Queue (With Capacity)](#queue-with-capacity)
  - [Queue (Linked List)](#queue-linked-list)
  - [Queue Comparison](#queue-comparison)
- [Other Data Structures](#other-data-structures)
- [Complexity Chart](#complexity-chart)
---
## Queue

### Queue (No Size Limit)

#### Methods

- `enqueue(item)`: Adds an item to the end.
- `dequeue()`: Removes and returns the front item.
- `peek()`: Returns the front item without removing it.
- `isEmpty()`: Checks if the queue is empty.
- `size()`: Returns the number of items.

#### Uses

- Print queues.
- Task scheduling.
- Breadth-first search.

---

### Queue (With Capacity)

#### Methods

- `enqueue(item)`: Adds an item if capacity allows.
- `dequeue()`: Removes and returns the front item.
- `peek()`: Returns the front item.
- `isEmpty()`: Checks if empty.
- `isFull()`: Checks if at capacity.
- `size()`: Returns current size.

#### Uses

- Bounded buffers (producer-consumer).
- Rate limiting.

#### Difference

- Enforces a maximum size; prevents overflow.

---

### Queue (Linked List)

#### Methods

- `enqueue(item)`: Adds to the end.
- `dequeue()`: Removes from the front.
- `peek()`: Returns front item.
- `isEmpty()`: Checks if empty.
- `size()`: Returns size.

#### Uses

- When dynamic resizing is needed.
- Avoids shifting elements (as in array-based queues).

#### Difference

- Backed by linked list; dynamic size, no shifting.

---

## Queue Comparison

| Implementation         | Enqueue | Dequeue | Peek   | Space Complexity | Notes                        |
|------------------------|---------|---------|--------|------------------|------------------------------|
| No Size (Array)        | O(1)*   | O(n)*   | O(1)   | O(n)             | Dequeue may require shifting |
| With Capacity (Array)  | O(1)    | O(1)    | O(1)   | O(k)             | Uses circular buffer         |
| Linked List            | O(1)    | O(1)    | O(1)   | O(1)             | Dynamic size, no shifting    |

\* If implemented naively, array-based dequeue is O(n) due to shifting. With circular buffer, it's O(1).

### Which is better?

- **With Capacity (Circular):** Best for fixed-size, high-performance needs (O(1) for all ops, minimal overhead).
- **Linked List:** Best for dynamic size, avoids overflow
- **No Size (Naive Array):** Simple, but dequeue is slow for large queues.

---
## Summary

- Use **queue with capacity** for fixed-size, high-performance needs.
- Use **linked list queue** for dynamic, unbounded queues.
- Avoid naive array queues for large or performance-critical applications.

