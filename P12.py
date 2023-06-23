# cherry pickup II
def cherryPickup(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[[float('-inf')] * cols for _ in range(cols)] for _ in range(rows)]
    
    
    def isValid(i, j):
        return 0 <= i < rows and 0 <= j < cols
    
    
    for i in range(cols):
        for j in range(cols):
            if isValid(rows-1, i) and isValid(rows-1, j):
                dp[rows-1][i][j] = grid[rows-1][i] + grid[rows-1][j]
    
    
    for row in range(rows-2, -1, -1):
        for i in range(cols):
            for j in range(cols):
                for x in [-1, 0, 1]: 
                    for y in [-1, 0, 1]: 
                        n_i = i + x
                        n_j = j + y
                        if isValid(row, n_i) and isValid(row, n_j):
                            dp[row][i][j] = max(dp[row][i][j], dp[row+1][n_i][n_j] + grid[row][i] + (grid[row][j] if i != j else 0))
    
    return dp[0][0][cols-1] 