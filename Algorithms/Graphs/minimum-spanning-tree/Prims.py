

#Prims alogrithm is used to find the minimum spanning tree of a graph.

import heapq
def prims(v, graph):
    # Create the adjacency list
    adj = [[] for _ in range(v)]
    for i in graph:
        adj[i[0]].append([i[1], i[2]])
        adj[i[1]].append([i[0], i[2]])
    
    visited = [False for _ in range(v)]
    pq = []
    sum = 0
    mst = []
    # push in the form of wt, node, parent
    heapq.heappush(pq, (0, 0, -1))

    while pq:
        dist, node, parent = heapq.heappop(pq)
        if visited[node]:
            continue
        if(parent == -1):
            visited[node] = True
        else:
            visited[node] = True
            mst.append([parent, node, dist])
            sum += dist
        
        # push all the adjacent nodes of the current node
        for i in adj[node]:
            # if the node is not visited, push it in the pq
            if not visited[i[0]]:
                # push in the form of wt, node, parent
                heapq.heappush(pq, (i[1], i[0], node))
        
    return mst, sum

    return

V = 5
graph = [[0,1,2], [0,2,1], [2,1,1], [2,4,2],[2,3,2], [4,3,1]]
print(prims(V, graph)) 