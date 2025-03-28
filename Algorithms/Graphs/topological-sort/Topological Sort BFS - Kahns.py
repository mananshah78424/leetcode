

def topologicalSort(graph):
    indegree = [0 for _ in range(len(graph))]

    for i in range(len(graph)):
        for j in graph[i]:
            indegree[j] += 1

    queue = []
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
        
    return result

graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0,1],
    5: [0,2]
}
print(topologicalSort(graph))


