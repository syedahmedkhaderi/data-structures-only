# Recursion

## 1. When is Recursion Used?
- In data structures like trees and graphs (traversal, searching, etc.)
- In sorting algorithms (e.g., quick sort, merge sort)
- In algorithms using divide and conquer, dynamic programming, and backtracking
- When a problem can be broken into similar subproblems

## 2. Why is Recursion Used?
- Simplifies code for problems that have a natural recursive structure
- Makes code easier to write and understand for hierarchical or nested problems
- Reduces the need for explicit stack management in many cases

## 3. Steps of Recursion
1. **Base Case:** Define a condition under which the recursion stops.
2. **Recursive Case:** The function calls itself with a simpler or smaller input.
3. **Progress:** Each call should bring the problem closer to the base case.

## 4. How Recursion Works
- Each recursive call adds a new frame to the call stack.
- When the base case is reached, the stack unwinds as each call returns.
- The process continues until all recursive calls have completed.

## 5. Tips to Understand Recursion
- Always identify and write the base case first.
- Trace the function with small inputs to see the call stack.
- Draw recursion trees to visualize the flow.
- Ensure each recursive call progresses toward the base case.
- Use print/debug statements to follow the execution order.

