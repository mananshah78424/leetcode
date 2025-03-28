


def dfs(graph, visited, stack, node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, visited, stack, i)
    stack.append(node)

def topologicalSort(graph):
    visited = [False for _ in range(len(graph))]
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, visited, stack, i)
    
    return stack[::-1]

graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0,1],
    5: [0,2]
}
print(topologicalSort(graph)) # [4, 5, 0, 2, 3, 1]
