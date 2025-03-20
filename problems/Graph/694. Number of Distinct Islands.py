# Find number of distinct islands 


def dfs(grid, i, j, path, visited, row0, col0):
    visited[i][j] = True
    path.append((i-row0, j-col0))

    for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
        nx, ny = i+dx, j+dy
        if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(grid, nx, ny, path, visited, row0, col0)
    

def bfs(grid, i, j, path, visited, row0, col0):
    visited[i][j] = True
    queue = [(i,j)]
    while queue:
        x,y = queue.pop(0)
        path.append((x-row0, y-col0))
        for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))

def numDistinctIslandsUsingDFS(grid):
    if not grid:
        return 0
    n = len(grid)
    m= len(grid[0])
    st = set()
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                path = []
                dfs(grid, i, j, path, visited, i, j)
                st.add(tuple(path))

    return len(st)

def numDistinctIslandsUsingBFS(grid):
    if not grid:
        return 0
    n = len(grid)
    m= len(grid[0])
    st = set()
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                path = []
                bfs(grid, i, j, path, visited, i, j)
                st.add(tuple(path))

    return len(st)

islands = [[1,1,0,1,1], [1,0,0,0,0], [0,0,0,1,1], [1,1,0,1,0]]
print(numDistinctIslandsUsingDFS(islands)) #2

print(numDistinctIslandsUsingBFS(islands)) #2