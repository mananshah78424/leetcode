

def dfs(grid, i, j, visited):
    visited[i][j] = True
    for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
        nx, ny = i+dx, j+dy
        if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == "1":
            dfs(grid, nx, ny, visited)


def bfs(grid,i,j,visited):
    visited[i][j]= True
    queue = [(i,j)]
    while(queue):
        x,y = queue.pop(0)
        for dx,dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            nx,ny = x+dx, y+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == "1":
                visited[nx][ny] = True
                queue.append((nx,ny))

def numIslands(grid):
    if not grid:
        return 0 
    
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == "1":
                count += 1
                dfs(grid, i, j, visited)
    
    return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid)) #1


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid)) #3