class Solution(object):
    def canPartition(self, nums):
        
        dp =set()
        dp.add(0)
        target = k
        for i in range(len(nums)-1, -1, -1):
            nextDP= set()
            for t in dp:
                nextDP.add(t+nums[i])
                if t+nums[i] == target:
                    return True
                else: 
                    False

            dp = nextDP
        return False

