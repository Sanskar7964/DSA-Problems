def minFallingPathSum(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0] = matrix[0]
        for i in range(1, rows):
            for j in range(cols):
                 if j == 0:
                   dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                 elif j == cols - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                 else:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])


        return min(dp[-1])