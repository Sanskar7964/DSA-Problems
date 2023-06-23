
def maximumNonAdjacentSum(nums):    
    
    temp1, temp2 = 0, 0

    for n in nums:
        res = max(n+temp1, temp2)
        temp1 = temp2
        temp2 = res

    return res