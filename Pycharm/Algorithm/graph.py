# A class to represent a graph object
class Graph:
    # Constructor to construct a graph
    def __init__(self, edges, n):

        # A list of lists to represent an adjacency list
        self.adjList = [None] * n

        # allocate memory for the adjacency list
        for i in range(n):
            self.adjList[i] = []

        # add edges to the directed graph
        for (src, dest, weight) in edges:
            # allocate node in adjacency list from src to dest
            self.adjList[src].append((dest, weight))


# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # print current vertex and all its neighboring vertices
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()


if __name__ == '__main__':
    # Input: Edges in a weighted digraph (as per the above diagram)
    # Edge (x, y, w) represents an edge from `x` to `y` having weight `w`
    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
             (4, 5, 1), (5, 4, 3)]

    # No. of vertices (labelled from 0 to 5)
    n = 6

    # construct a graph from a given list of edges
    graph = Graph(edges, n)

    # print adjacency list representation of the graph
    printGraph(graph)