# Use min-heap to solve this


import heapq
def dijkstra(graph, start, n):
    adj = [[] for _ in range(n)]
    for i in graph:
        adj[i[0]].append([i[1], i[2]])
        adj[i[1]].append([i[0], i[2]])
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        d, node = heapq.heappop(pq)
        for i in adj[node]:
            if dist[i[0]] > d+i[1]:
                dist[i[0]] = d+i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
    
    return dist
                         


graph = [[0,1,4], [0,2,4], [1,2,2], [2,3,3], [3,5,2], [4,5,3], [2,4,1], [2,5,6]]
# n is the number of vertices
n = 6
print(dijkstra(graph, 0, n)) # [0, 1, 2, 3]

# Time Complexity: O(E log V)
# Space Complexity: O(V)
# Stable: No
# In-place: No
# Adaptive: No
# Used in: Dijkstra's algorithm is used in the shortest path algorithm.