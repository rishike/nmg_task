
# Floyd - Warshall Algorithm
# A[i,j] = min(A[i, j], A[i,k] + A[k,j])

import numpy as np
from math import inf


class FloydWarshall():
    def __init__(self, graph):
        self.graph = graph

    def print(self):
        return np.matrix(self.graph)

    def algorithm(self):
        rows = len(self.graph)

        for k in range(0, rows):
            for i in range(0, rows):
                for j in range(0, rows):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

    def print_shortest_path(self, i, j):
        if i >= len(self.graph) or j >= len(self.graph[0]):
            print("Index out of range")
            return
        if i == j:
            print(self.graph[i][j])
            return
        elif self.graph[i][j] == inf:
            print(f"No path from {i} to {j}")
            return
        else:
            self.print_shortest_path(i, self.graph[i][j])
            print(f"{j}->")

    def __str__(self):
        return str(np.matrix(self.graph))

# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 3, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 7, 0, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 1, 0]
    ]

    result = floyd_warshall(graph)

    # shortest distances between all pairs of vertices
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(f"Shortest distance from vertex {i} to vertex {j}: {result[i][j]}")
