def minCost(stones):

    # for i in range(n-1):
    #     fs = dp[i-1] + abs(height[i] - heights[i-1]):
    #     ss = max
    #     if(i>1):
    #         ss

    n = len(stones)
    memo = [-1]*n
    memo[0] = 0
    memo[1] = abs(stones[1] - stones[0])
    return helper(stones, n-1, memo)

def helper(stones, index, memo):
    if memo[index] != -1:
        return memo[index]
    
    price1 = helper(stones, index-1, memo) +abs(stones[index] - stones[index-1])
    price2 = helper(stones, index-2, memo ) +abs(stones[index]- stones[index-2] )

    memo[index] = min(price1, price2)
    return memo[index]

