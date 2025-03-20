# Detect cycle in graph using BFS


def detectCycle(graph, visited):
    
    visited[0] = 1
    queue = [(0, -1)]
    while queue:
        node, parent = queue.pop(0)
        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i, node))
            elif parent != i:
                return True
            
    return False

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0,3],
    3: [1,2]
}

visited = [0 for _ in range(len(graph))]
for i in range(len(graph)):
    if not visited[i]:
        if detectCycle(graph, visited):
            print("Cycle detected")
        else:
            print("No cycle detected")
