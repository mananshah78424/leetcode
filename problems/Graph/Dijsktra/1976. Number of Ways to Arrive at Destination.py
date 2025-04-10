# Algorithm 
# 1. Use a distance and a ways array to keep track of the shortest distance and number of ways to reach each node.
import heapq
def countPaths(n,edges):
    dist = [float('inf')] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1
    adj = [[] for _ in range(n)]  
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    pq = []
    heapq.heappush(pq, (0, 0))  # (distance, node)
    while pq:
        d, node = heapq.heappop(pq)
        for nei, weight in adj[node]:
            new_dist = d + weight
            if new_dist == dist[nei]:
                ways[nei] += ways[node]
            elif new_dist < dist[nei]:
                dist[nei] = new_dist
                ways[nei] = ways[node]
                heapq.heappush(pq, (new_dist, nei))
    return ways[n-1] % 1000000007
    
n=7
edges = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(countPaths(n, edges)) # 4