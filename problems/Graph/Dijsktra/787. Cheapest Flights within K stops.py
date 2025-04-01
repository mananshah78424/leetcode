

import heapq

#Approach: Use Dijkstra's algorithm to find the shortest path from source to destination.
def findCheapestPrice(n, flights, src, dst, k):
    adj = [[] for _ in range(n)]
    for u, v, w in flights:
        adj[u].append((v, w))

    # Min-heap: (cost, node, remaining stops)
    pq = [(0, src, k + 1)]  # k+1 because we count edges, not nodes
    
    # Distance dictionary to track min cost to reach a node with a given stop count
    dist = {}

    while pq:
        cost, node, stops = heapq.heappop(pq)
        
        if node == dst:
            return cost
        
        if stops > 0:
            for neighbor, price in adj[node]:
                new_cost = cost + price
                # Only push to heap if new_cost is better for given stop count
                if (neighbor, stops - 1) not in dist or new_cost < dist[(neighbor, stops - 1)]:
                    dist[(neighbor, stops - 1)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops - 1))
    
    return -1


flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n = 4, flights = flights, src = src, dst = dst, k = k)) #700