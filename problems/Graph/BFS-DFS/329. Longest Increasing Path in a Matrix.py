


def longestIncreasingPath(matrix):
    def dfs(i,j, cache, matrix):
        if cache[i][j] > 0:
            return cache[i][j]
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        max_length = 0
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and matrix[nx][ny] > matrix[i][j]:
                longest = dfs(nx, ny, cache, matrix)
                max_length = max(max_length, longest)
                print(max_length, longest, i, j, nx, ny)
        cache[i][j] = max_length + 1
        return cache[i][j]
    
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    cache = [[0]*n for _ in range(m)]
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i,j, cache, matrix))
    return res
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix)) # 4