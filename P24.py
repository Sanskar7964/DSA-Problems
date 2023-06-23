def rodCutting(lengths, prices, rod_length):
    n = len(lengths)
    dp = [0] * (rod_length + 1)

    for i in range(1, rod_length + 1):
        for j in range(n):
            if lengths[j] <= i:
                dp[i] = max(dp[i], prices[j] + dp[i - lengths[j]])

    return dp[rod_length]