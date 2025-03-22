# Keep two arrays, visted and pathVisited

def dfs(graph, visited, pathVisited, node):
    visited[node] = 1
    pathVisited[node] = 1
    # traverse for adjacent nodes
    for i in graph[node]:
        # when node is not visited
        if not visited[i]:
            if dfs(graph, visited, pathVisited,i):
                return True
        # if prev visited, but has been visited on the same path
        elif pathVisited[i]:
            return True
    pathVisited[node] = 0

    return False

def cycleDetection(graph):
    visited = [0 for _ in range(len(graph))]
    pathVisited = [0 for _ in range(len(graph))]
    for i in range(1, len(graph)):
        if not visited[i]:
            if dfs(graph, visited, pathVisited, i):
                return True
    return False

graph = {
    1: [2],
    2: [3],
    3: [4,7],
    4: [5],
    5: [6],
    6: [],
    7: [5],
    8: [9],
    9: [10],
    10: [8]
}
print(cycleDetection(graph)) #False