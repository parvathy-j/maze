# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List, Dict, Tuple

from maze.util import Coordinates
from maze.graph import Graph

class AdjListGraph(Graph):
    def __init__(self):
        # Initialize the adjacency list as an empty dictionary.
        # Each key (vertex) maps to a list of tuples (neighboring vertex, wall status).
        self.adjList: Dict[Coordinates, List[Tuple[Coordinates, bool]]] = {}

    def addVertex(self, label: Coordinates):
        # Add a vertex to the graph if it does not already exist.
        if label not in self.adjList:
            self.adjList[label] = []

    def addVertices(self, vertLabels: List[Coordinates]):
        # Add multiple vertices to the graph.
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        # Add an edge between two vertices with an optional wall.
        if vert1 in self.adjList and vert2 in self.adjList:
            # Avoid adding duplicate edges
            if vert2 not in [neigh for neigh, _ in self.adjList[vert1]]:
                self.adjList[vert1].append((vert2, addWall))
                self.adjList[vert2].append((vert1, addWall))
                return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        # Update the wall status between two vertices.
        updated = False
        for vert, neigh in [(vert1, vert2), (vert2, vert1)]:
            for i, (neighVert, _) in enumerate(self.adjList.get(vert, [])):
                if neighVert == neigh:
                    self.adjList[vert][i] = (neigh, wallStatus)
                    updated = True
        return updated

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Remove the edge between two vertices.
        removed = False
        for vert, neigh in [(vert1, vert2), (vert2, vert1)]:
            initialLength = len(self.adjList.get(vert, []))
            self.adjList[vert] = [(neighVert, wall) for neighVert, wall in self.adjList.get(vert, []) if neighVert != neigh]
            if len(self.adjList[vert]) < initialLength:
                removed = True
        return removed

    def hasVertex(self, label: Coordinates) -> bool:
        # Check if the graph contains a vertex.
        return label in self.adjList

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Check if there is an edge between two vertices.
        return any(neigh == vert2 for neigh, _ in self.adjList.get(vert1, []))

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # Get the wall status between two vertices.
        for neigh, wallStatus in self.adjList.get(vert1, []):
            if neigh == vert2:
                return wallStatus
        # If there's no such edge, assume there's no wall (open path).
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        # Return a list of neighbors for a given vertex.
        return [neigh for neigh, _ in self.adjList.get(label, [])]
