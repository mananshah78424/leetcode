# Since same time its happening and same levels - BFS
# Use a queue since BFS
# Starting point is wherever a rotten orange is
# Visited 2D array to keep track of visited oranges


def orangesRotting(grid):
    n = len(grid)
    m = len(grid[0])

    # Find all rotten oranges and store in queue 
    queue = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                # lets add the time with index to queue
                queue.append([i,j,0])
                visited[i][j] = True

    # BFS
    res = 0
    while queue:
        x,y,time = queue.pop(0)
        # Check all 4 directions
        for dx,dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([nx,ny,time+1])
                res = max(res, time+1)
    
    # Check if there are any fresh oranges left
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                return -1
            
    return res

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid)) #4