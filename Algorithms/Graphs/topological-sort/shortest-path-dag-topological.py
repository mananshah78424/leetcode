


def dfs(graph, visited, stack, node):
    visited[node] = True
    for it in graph[node]:
        if not visited[it[0]]:
            dfs(graph, visited, stack, it[0])
    stack.append(node)

def shortestPath(n, edges):
    # Create the adjacency list
    adj = [[] for _ in range(n)]
    for i in edges:
        adj[i[0]].append([i[1], i[2]])

    visited = [False for _ in range(n)]
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(adj, visited, stack, i)

    # Find the distance array
    dist = [float('inf') for _ in range(n)]
    dist[0] = 0
    
    print(stack)
    while stack:
        node = stack.pop()
        for i in adj[node]:
            print(node, adj[node])
            dist[i[0]] = min(dist[i[0]], dist[node]+i[1])
    
    return dist

    

edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]]
n = 6
print(shortestPath(n,edges)) # [0, 2, 5, 6, 1, 5]