# Here we will build an undirected graph using an adjacency list.
class Graph:

#The constructior will initialize the number of vertices in the graph to zero and the adjcency list to an empty dictionary
    def __init__(self) -> None:
        self.no_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            self.no_of_nodes += 1
            return
    
#Next we will implement the insert edge method where we will specify two nodes between which an edge is to be added.
#First we will check if an edge already exists by checking the adjacency list of either of the two nodes.
#If the other node is present it means the edge already exists, if not then the edge doesn't exist.
#So we add the edge by adding the complimentary node in the adjacency list of either node
    def insert_edge(self, vertex1, vertex2):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return
        return "Edge already exists"
    
#Finally we will implement a custom print method which willl print the nodes and their connections
    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')

my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_edge(1,2)
my_graph.insert_edge(1,3)
my_graph.insert_edge(2,3)
my_graph.show_connections()

"""
1 -->> 2 3
2 -->> 1 3
3 -->> 1 2
"""

print(my_graph.adjacency_list)
#{1: [2, 3], 2: [1, 3], 3: [1, 2]}

print(my_graph.number_of_nodes)
#3