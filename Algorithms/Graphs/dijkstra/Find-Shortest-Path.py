#Print shortest path in Weighted undirected graph
import heapq
def shortestPath(graph, V):
    adj = [[] for _ in range(V)]
    for i in graph:
        adj[i[0]].append([i[1], i[2]])
        adj[i[1]].append([i[0], i[2]])
    
    dist = [float('inf') for _ in range(V)]
    parent = [i for i in range(V)]
    dist[1] = 0

    pq = []
    heapq.heappush(pq, (0, 1))
    while pq:
        d, node = heapq.heappop(pq)
        for i in adj[node]:
            if dist[i[0]] > dist[node]+i[1]:
                dist[i[0]] = dist[node]+i[1]
                parent[i[0]] = node
                heapq.heappush(pq, (dist[i[0]], i[0]))
    
    # Now we have shortest distance
    # Lets use parent array to find the path
    res = []
    node = V-1
    while(parent[node]!=node):
        res.append(node)
        node = parent[node]
    res.append(1)
    return res[::-1]


edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1], [4,3,3], [3,5,1]]
V = 6
print(shortestPath(edges, V)) # [0, 1, 4, 3, 5]