def minCost2(stones, k):
    
    n = len(stones)
    memo = [-1]*n
    memo[0] = 0
    memo[1] = abs(stones[1] - stones[0])
    return helper(stones, n-1, k, memo)

def helper(stones, index, k, memo):
    if memo[index] != -1:
        return memo[index]
    
    cost = float('inf')
    for i in range(1, k-1):
        if index -1>=0:
    
            price = helper(stones, index-1,k, memo) +abs(stones[index] - stones[index-1])


    memo[index] = min(price)
    return memo[index]

