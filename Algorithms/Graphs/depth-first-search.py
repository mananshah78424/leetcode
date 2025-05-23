# Depth first search algorithm


def dfs(graph, start):
    visited = []
    res = []
    stack = [start]
    while stack:
        node = stack.pop()
        res.append(node)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append(neighbour)
    
    return res

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'F', 'C']

# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Stable: No
# In-place: No
# Adaptive: No
# Used in: Depth-first search is used in the depth-first search algorithm.
