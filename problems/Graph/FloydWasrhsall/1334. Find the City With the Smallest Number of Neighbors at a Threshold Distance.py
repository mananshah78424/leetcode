

def findTheCity(n, edges, distanceThreshold):
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u,v,w in edges:
        dist[u][v]=w
        dist[v][u]=w

    for via in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][via] + dist[via][j]:
                    dist[i][j] = dist[i][via] + dist[via][j]
    
    res=float('inf')
    city = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if dist[i][j] <= distanceThreshold:
                count += 1
        if count <= res:
            res = count
            city = i
    return city

edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
n = 4
distanceThreshold = 4
print(findTheCity(n, edges, distanceThreshold)) # 3