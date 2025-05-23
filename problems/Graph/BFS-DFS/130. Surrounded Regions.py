


# 130. Surrounded Regions
# Solve using BFS algorithm

def checkIfBorder(i,j,n,m):
    if i==0 or j==0 or i==n-1 or j==m-1:
        return True
    return False

def solve(board):
    n=len(board)
    m=len(board[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = []
    # Find all border "O" cells and mark them as visited
    for i in range(n):
        for j in range(m):
            if board[i][j] == "O" and checkIfBorder(i,j,n,m):
                queue.append((i,j))
                visited[i][j] = True
    # BFS to mark all "O" cells connected to the border
    while queue:
        x,y = queue.pop(0)
        for dx,dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == "O":
                visited[nx][ny] = True
                queue.append((nx,ny))
    # Change all unvisited "O" cells to "X" and visited "X" cells back to "O"
    for i in range(n):
        for j in range(m):
            if board[i][j] == "O" and not visited[i][j]:
                board[i][j] = "X"

    return board


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(solve(board)) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]