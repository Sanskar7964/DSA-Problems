def count_subsets_with_sum(arr, K):
    n = len(arr)
    dp = [[0] * (K + 1) for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= arr[i - 1]:
                dp[i][j] += dp[i - 1][j - arr[i - 1]]

    return dp[n][K]
