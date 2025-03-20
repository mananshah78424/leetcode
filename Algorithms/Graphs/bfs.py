# Implement breadth first search algorithm

def bfs(graph, start):
    visited = []
    res=[]
    queue = [start]
    while queue:
        node = queue.pop(0)
        res.append(node)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
        
    return res

    

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']