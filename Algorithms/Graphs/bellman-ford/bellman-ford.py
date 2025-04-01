

def bellmanFord(graph, V):
    
    dist = [float('inf') for _ in range(V)]
    dist[0] = 0
    # Time complexity: O(V*E)
    for i in range(V-1):
        for u, v, w in graph:
            if dist[u]!=float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    #Check for negative cycles - only Nth cycle will have an effect
    for u, v, w in graph:
        if dist[u]!=float('inf') and dist[u] + w < dist[v]:
            return []
    
    return dist

graph = [[0,1,4], [0,2,4], [1,2,2], [2,3,3], [3,5,2], [4,5,3], [2,4,1], [2,5,6]]
V = 6
print(bellmanFord(graph, V)) # [0, 1, 2, 3]