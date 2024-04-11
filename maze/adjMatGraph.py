# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------
from typing import List
from maze.util import Coordinates
from maze.graph import Graph

from typing import List
from maze.util import Coordinates
from maze.graph import Graph



class AdjMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overridden methods are meant to do.
    """
    def __init__(self):
        # Initialize an empty adjacency matrix
        self.adj_matrix = {}

    def addVertex(self, label: Coordinates):
        # Add a vertex to the adjacency matrix
        if label not in self.adj_matrix:
            self.adj_matrix[label] = {}

    def addVertices(self, vertLabels: List[Coordinates]):
        # Add multiple vertices to the adjacency matrix
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        # Add an edge between two vertices in the adjacency matrix
        print("Add edge")
        if vert1 in self.adj_matrix and vert2 in self.adj_matrix:
            self.adj_matrix[vert1][vert2] = not addWall
            self.adj_matrix[vert2][vert1] = not addWall
            return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        print(f"Updating wall between {vert1} and {vert2}, wallStatus={wallStatus}")
        # Update the wall status between two vertices
        if vert1 in self.adj_matrix and vert2 in self.adj_matrix:
            self.adj_matrix[vert1][vert2] = not wallStatus  # Invert wall status when updating
            self.adj_matrix[vert2][vert1] = not wallStatus  # Invert wall status when updating
            print("Updated wall")
            return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        print(f"Removing edge between {vert1} and {vert2}")
        # Remove an edge between two vertices
        if vert1 in self.adj_matrix and vert2 in self.adj_matrix:
            self.adj_matrix[vert1][vert2] = True
            self.adj_matrix[vert2][vert1] = True
            print("Edge removed")
            return True
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        print(f"Checking if vertex {label} exists")
        # Check if a vertex exists in the adjacency matrix
        return label in self.adj_matrix

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Check if an edge exists between two vertices
        if vert1 in self.adj_matrix and vert2 in self.adj_matrix:
            return vert2 in self.adj_matrix[vert1]
        return False

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Get the wall status between two vertices
        if vert1 in self.adj_matrix and vert2 in self.adj_matrix:
            return not self.adj_matrix[vert1][vert2]
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        # Get the neighbors of a vertex
        if label in self.adj_matrix:
            return [v for v, wall in self.adj_matrix[label].items() if not wall]
        return []
#     def isPerfect(self) -> bool:
#         visited = set()
#
#         def dfs(v, parent=None):
#             if v in visited:
#                 return False
#             visited.add(v)
#             for neighbour in self.neighbours(v):
#                 if neighbour != parent:
#                     if not dfs(neighbour, v):
#                         return False
#             return True
#
#         start_vertex = self.vertices[0] if self.vertices else None
#         if not start_vertex or not dfs(start_vertex):
#             return False  # Either not connected or has a cycle
#
#         # Ensure every vertex has been visited to confirm full connectivity
#         return len(visited) == len(self.vertices)
# graph = AdjMatGraph()
# print(graph.isPerfect())
