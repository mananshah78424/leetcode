


def floydWarshall(graph, V):
    # Create a 2D list of size V x V and initialize it with infinity
    dist = [[float('inf') for _ in range(V)] for _ in range(V)]

    # Initialize the diagonal elements to 0
    for i in range(V):
        dist[i][i] = 0

    # Fill the distance array with the input graph
    for u,v,w in graph:
        dist[u][v] = w

    # Choose an intermediate vertex k and check if the shortest path from i to j is via k
    for via in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][via] + dist[via][j]:
                    dist[i][j] = dist[i][via] + dist[via][j]
    
    return dist

graph = [[0,1,4], [0,2,4], [1,2,2], [2,3,3], [3,5,2], [4,5,3], [2,4,1], [2,5,6]]
V = 6
print(floydWarshall(graph, V)) # [0, 1, 2, 3]