#count squres

def countSquares(self, matrix: List[List[int]])-> int:
    n = len(matrix)
    m= len(matrix[0])
    dp = [[0]*(m+1) for _ in range(n+1)]
    count = 0

    for row in range(1, n+1):
        for col in range(1, m+1):
            if matrix[row-1][col-1] == 1:
                dp[row][col] = 1+ min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1] )
                count+= dp[row][col]

    return count