def unboundedKnapsack(W, weights, values):
    n = len(weights)
    dp = [0]*(W+1)

    for i in range(W+1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i-weights[j]]+values[j])

    return dp[W]
# read this problem again!!!

