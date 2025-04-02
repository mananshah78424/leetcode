def kruskal(V, graph):
    # Sort the edges based on weight
    graph.sort(key=lambda x: x[2])

    # Disjoint set data structure
    parent = [i for i in range(V)]
    rank = [0] * V

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        xroot = find(x)
        yroot = find(y)

        if xroot != yroot:  # Only union if they are in different sets
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

    mst = []
    total_weight = 0

    for u, v, w in graph:
        if find(u) != find(v):
            mst.append((u, v, w))
            union(u, v)
            total_weight += w

    return mst, total_weight

# Example graph (edges: [u, v, weight])
graph = [[5,4,9], [5,1,4], [4,1,1], [4,2,3], [1,2,2], [4,3,5], [3,2,3],[3,6,8],[2,6,7]]
V = 7

print(kruskal(V, graph))
