

import heapq
def minimumEffortPath(heights):
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    n = len(heights)
    m = len(heights[0])
    dist = [[float('inf') for _ in range(m)] for _ in range(n)]
    dist[0][0] = 0

    while pq:
        d,x,y = heapq.heappop(pq)
        # Since its a PQ, the moment we reach the destination, we can return the distance
        if x == n-1 and y == m-1:
            return d
            
        
        # Traverse all the 4 directions 
        for dx,dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            nx, ny = x+dx, y+dy 
            if 0<=nx<n and 0<=ny<m:
                neweffort = max(d, abs(heights[x][y]-heights[nx][ny]))
                if(neweffort < dist[nx][ny]):
                    dist[nx][ny] = neweffort
                    heapq.heappush(pq, (neweffort, nx, ny))

            
        
    return -1


heights = [[1,10,6,7,9,10,4,9]]


print(minimumEffortPath(heights)) # 2