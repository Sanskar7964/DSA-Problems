
def minPathSum(self, grid):
     
  
        M, N = len(grid), len(grid[0])
        res = [[float("inf")]*(N+1) for r in range(M+1)]
        res[M-1][N] = 0

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
  
        return res[0][0]