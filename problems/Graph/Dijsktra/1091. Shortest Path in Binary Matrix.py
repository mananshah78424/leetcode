

def shortestPathBinaryMatrix(graph):
    # Since n*n matrix 
    dist = [[float('inf') for _ in range(len(graph))] for _ in range(len(graph))]
    dist[0][0] = 1
    # Dist, x, y
    queue = [[1,0,0]]
    while queue and dist[-1][-1] == float('inf'):
        d,x,y = queue.pop(0)
        # Check all 8 directions
        for dx,dy in [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]:
            nx, ny = x+dx, y+dy
            if(0<=nx<len(graph) and 0<=ny<len(graph[0]) and graph[nx][ny]==0):
                # Check if distance is lesser
                if(dist[nx][ny]> d + 1):
                    dist[nx][ny] = d + 1
                    queue.append([d+1, nx, ny])
    return dist[-1][-1] if dist[-1][-1]!=float('inf') else -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid)) # 4