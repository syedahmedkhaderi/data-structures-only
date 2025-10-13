# Graph Data Structures in Python

This repository contains multiple Python implementations for undirected graph data structures using adjacency lists. The included code demonstrates how to create nodes (vertices), add edges, and display graph connections. These implementations provide a foundation for further development in network analysis, algorithm practice, or educational use.

## Features

- Object-oriented design with classes for graph representation.
- Support for dynamic insertion of nodes and undirected edges.
- Adjacency list representations to store connections efficiently.
- Methods to visualize and print graph connectivity.
- Practical usage examples within each script.

## File Overview

### `graphs.py`

- Provides an undirected graph implementation with:
  - Method to insert nodes (`insert_node`)
  - Method to insert edges (`insert_edge`)
  - Method to print the adjacency list (`show_connections`)
- Comments and example usage provided within the file.
- Maintains total number of nodes via `no_of_nodes`.
- Adjacency list is a `dict` mapping nodes to neighbor lists.

### `minimalist_graphs.py`

- Alternate minimalist implementation with:
  - Methods to add vertices (`addVertex`)
  - Methods to add edges (`addEdge`)
  - Method to print all connections (`showConnection`)
- Uses a dictionary (`adjacentlist`) for adjacency structure.
- Designed for simplicity and readability.

## Usage

1. Clone this repository and extract the files.
2. Import or run the scripts in your Python environment (Python 3.x recommended).
3. Review the comments and example code for guidance.
4. Modify the graphs or add custom methods to suit project needs.

